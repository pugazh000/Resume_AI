# resume_jobmatcher/src/tokenizer.py
import re

class SimpleTokenizer:
    def __init__(self):
        self.vocab = {}

    def fit(self, texts):
        index = 0
        for text in texts:
            tokens = self._tokenize(text)
            for token in tokens:
                if token not in self.vocab:
                    self.vocab[token] = index
                    index += 1

    def transform(self, texts):
        return [[self.vocab.get(token, -1) for token in self._tokenize(text)] for text in texts]

    def _tokenize(self, text):
        return re.findall(r'\b\w+\b', text.lower())

