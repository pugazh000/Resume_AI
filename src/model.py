# resume_jobmatcher/src/model.py
import numpy as np

class LogisticRegressionScratch:
    def __init__(self, input_dim, output_dim):
        self.W = np.zeros((input_dim, output_dim))
        self.b = np.zeros(output_dim)

    def softmax(self, z):
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def predict(self, X):
        z = np.dot(X, self.W) + self.b
        return self.softmax(z)

    def train(self, X, y, epochs=100, lr=0.01):
        y_onehot = np.eye(self.b.shape[0])[y]
        for _ in range(epochs):
            logits = self.predict(X)
            error = logits - y_onehot
            grad_W = np.dot(X.T, error) / len(X)
            grad_b = np.mean(error, axis=0)
            self.W -= lr * grad_W
            self.b -= lr * grad_b

