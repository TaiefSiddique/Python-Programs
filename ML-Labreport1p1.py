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
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

best_k = None
best_avg = 0

for k in range(1, 15):
    scores = {}
    scores_list = []

    for _ in range(10):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
        scaler = StandardScaler()
        scaler.fit(X_train)
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)
        
        classifier = KNeighborsClassifier(n_neighbors=k)
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        
        scores[k] = metrics.accuracy_score(y_test, y_pred)
        scores_list.append(metrics.accuracy_score(y_test, y_pred))
        
        #result = metrics.confusion_matrix(y_test, y_pred)
        #result1= metrics.classification_report(y_test, y_pred)
        #print("Confusion_Matrix : ")
        #print(result)
        #print("Classification_Report : ")
        #print(result1)
        
    plt.plot(scores_list)
    plt.xlabel("Value_of_K")
    plt.ylabel("Accuracy")
    
    avg_accuracy = p.mean(scores_list)
    if avg_accuracy > best_avg:
        best_avg = avg_accuracy
        best_k = k

print("Best K:", best_k)
print("Best Average Accuracy:", best_avg)
