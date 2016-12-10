import numpy as np


class RandomPredictor:

    def fit(self, X, y):
        self.classes_, counts = np.unique(y, return_counts=True)
        self.weights = counts / counts.sum()

        p = np.full(len(self.classes_), 0.5).cumprod()
        self.fake_output_probabilities = p / p.sum()
        return self

    def predict(self, X):
        return np.random.choice(self.classes_, len(X), p=self.weights, replace=True)

    def predict_proba(self, X):
        n = len(self.classes_)
        output_probs = np.empty((len(X), n))
        for i in range(len(X)):
            # Randomly choose classes, based on weights. This actually gets the index of each class instead of the class
            ixs = np.random.choice(n, p=self.weights, size=n, replace=False)
            # Arrange the probabilities so that they're in the correct order
            output_probs[i, ixs] = self.fake_output_probabilities
        return output_probs
