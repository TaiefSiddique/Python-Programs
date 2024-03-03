import numpy as p
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

iris = load_iris()
print(iris.feature_names)
print(iris.target)
print(iris.target_names)
print(iris.data.shape)

X = iris.data[:, :4]
y = iris.target

scaler = StandardScaler()

best_ratio = None
best_avg = 0

for ratio in p.arange(0.01, 0.6, 0.1):
    scores = {}
    scores_list = []
    for _ in range(10):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=ratio)
        scaler = StandardScaler()
        scaler.fit(X_train)
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)
        
        classifier = KNeighborsClassifier(n_neighbors=best_k)
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        
        scores[k] = metrics.accuracy_score(y_test, y_pred)
        scores_list.append(metrics.accuracy_score(y_test, y_pred))

    plt.plot(scores_list, label=f"Test Set Ratio={ratio}")

    avg_accuracy = p.mean(scores_list)
    if avg_accuracy > best_avg:
        best_avg = avg_accuracy
        best_ratio = 1 - ratio

print("Best Test Set Ratio:", ratio)
print("Best Training Set Ratio:", best_ratio)
print("Best Average Accuracy:", best_avg)

plt.xlabel("Iteration")
plt.ylabel("Accuracy")
plt.legend()
plt.show()
