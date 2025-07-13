# resumeproject/src/train.py

import os
import pandas as pd
import numpy as np
import pickle
from tokenizer import SimpleTokenizer
from featurizer import TFIDFFeaturizer
from model import LogisticRegressionScratch
from sklearn.preprocessing import LabelEncoder

# ✅ Path to CSV and extracted resume texts
csv_path = "/content/drive/MyDrive/resumeproject/data/resume_labeled.csv"
text_dir = "/content/drive/MyDrive/resumeproject/data/resumes/extracted_texts"

# ✅ Output path to save model and components
save_dir = "/content/drive/MyDrive/resumeproject/data/processed"
os.makedirs(save_dir, exist_ok=True)

# Load resume text data and labels
texts = []
labels = []

df = pd.read_csv(csv_path)
for row in df.itertuples():
    path = os.path.join(text_dir, row.filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            texts.append(f.read())
            labels.append(row.category)

# ✅ Print class distribution
from collections import Counter
print("📊 Class counts:", Counter(labels))

# Tokenize resumes
tokenizer = SimpleTokenizer()
tokenizer.fit(texts)
tokenized = tokenizer.transform(texts)

# TF-IDF Featurization
featurizer = TFIDFFeaturizer()
featurizer.fit(tokenized)
X = featurizer.transform(tokenized)

# Encode labels (job categories)
le = LabelEncoder()
y = le.fit_transform(labels)

# Train logistic regression model from scratch
print("🚀 Training with 10 epochs...")
model = LogisticRegressionScratch(X.shape[1], len(le.classes_))
model.train(X, y,epochs=10)

# ✅ Save model weights
np.savez(os.path.join(save_dir, "model_weights.npz"), W=model.W, b=model.b)

# ✅ Save tokenizer vocabulary
with open(os.path.join(save_dir, "tokenizer.pkl"), "wb") as f:
    pickle.dump(tokenizer.vocab, f)

# ✅ Save label encoder
with open(os.path.join(save_dir, "label_encoder.pkl"), "wb") as f:
    pickle.dump(le, f)

print("✅ Training complete and model saved to:", save_dir)
