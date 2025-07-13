# resume_jobmatcher/src/featurizer.py
from collections import Counter
import numpy as np
import math

class TFIDFFeaturizer:
    def fit(self, documents):
        self.df = {}
        self.idf = {}
        self.N = len(documents)
        for doc in documents:
            unique_tokens = set(doc)
            for token in unique_tokens:
                self.df[token] = self.df.get(token, 0) + 1
        for token in self.df:
            self.idf[token] = math.log(self.N / (1 + self.df[token]))

    def transform(self, documents):
        features = []
        for doc in documents:
            tf = Counter(doc)
            vec = [tf.get(token, 0) * self.idf.get(token, 0) for token in self.idf]
            features.append(vec)
        return np.array(features)
