import numpy as np
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Euclidean Distance Function
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Custom KNN Classifier Class
class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = np.array(X)
        self.y_train = np.array(y)

    def predict(self, X):
        return [self._predict(x) for x in X]

    def _predict(self, x):
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_labels = [self.y_train[i] for i in k_indices]
        return Counter(k_labels).most_common(1)[0][0]

# --- TASK 1

iris = load_iris()
X = iris.data  
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("--- TASK 1: Iris Dataset successfully loaded and split! ---")
print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}\n")

# --- TASK 2
k_values = [1, 3, 5, 7]
print("--- TASK 2: Comparing Accuracy for k = 1, 3, 5, 7 ---")

for k in k_values:
    
    model = KNN(k=k)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)
    print(f"k = {k}  -->  Accuracy: {acc * 100:.2f}%")