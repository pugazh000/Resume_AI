# resume_jobmatcher/src/predict.py
import os
import fitz  # PyMuPDF
import numpy as np
import pickle
import re
from collections import Counter

# Load model & components
base = "/content/drive/MyDrive/resumeproject/data/processed"
weights = np.load(os.path.join(base, "model_weights.npz"))
W = weights["W"]
b = weights["b"]

with open(os.path.join(base, "tokenizer.pkl"), "rb") as f:
    vocab = pickle.load(f)

with open(os.path.join(base, "label_encoder.pkl"), "rb") as f:
    le = pickle.load(f)

# Resume preprocessor
class PredictTokenizer:
    def __init__(self, vocab):
        self.vocab = vocab

    def tokenize(self, text):
        return [self.vocab.get(token, -1) for token in re.findall(r'\b\w+\b', text.lower())]

class Predictor:
    def __init__(self, W, b, vocab, le):
        self.W = W
        self.b = b
        self.vocab = vocab
        self.le = le

    def featurize(self, tokens):
        tf = Counter(tokens)
        N = 1
        df = {token: 1 for token in self.vocab}  # approximate
        idf = {token: np.log(N / (1 + df[token])) for token in self.vocab}
        vec = [tf.get(token, 0) * idf.get(token, 0) for token in self.vocab]
        return np.array([vec])

    def predict(self, text):
        tokens = PredictTokenizer(self.vocab).tokenize(text)
        x = self.featurize(tokens)
        z = x.dot(self.W) + self.b
        probs = np.exp(z) / np.sum(np.exp(z))
        return self.le.inverse_transform([np.argmax(probs)])[0]

# Example usage: predict from text or PDF
predictor = Predictor(W, b, vocab, le)

# Predict from a TXT file
txt_path = "/content/drive/MyDrive/resumeproject/data/resumes/extracted_texts/ACCOUNTANT_045.txt"
with open(txt_path, "r", encoding="utf-8") as f:
    resume_text = f.read()

prediction = predictor.predict(resume_text)
print("📄 Predicted Category:", prediction)
