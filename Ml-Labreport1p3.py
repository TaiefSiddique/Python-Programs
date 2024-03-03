import numpy as p
from sklearn import metrics
from google.colab import drive
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

#drive.mount('/content/MyDrive')

df = pd.read_csv("/content/MyDrive/My Drive/Dataset/Colab file/fish.csv")
X_fish = df.drop(columns=['Species'])
y_fish = df['Species']

print(df.shape)
print(df.columns)

X_train_fish, X_test_fish, y_train_fish, y_test_fish = train_test_split(X_fish, y_fish)

scaler_fish = StandardScaler()
scaler_fish.fit(X_train_fish)
X_train_fish = scaler_fish.transform(X_train_fish)
X_test_fish = scaler_fish.transform(X_test_fish)

print(X_train_fish.shape)
print(X_test_fish.shape)
print(y_train_fish.shape)
print(y_test_fish.shape)

best_ratio = None
best_avg = 0

for ratio in p.arange(0.01, 0.95, 0.1):
    scores = {}
    scores_list = []
    for _ in range(10):
        X_train, X_test, y_train, y_test = train_test_split(X_fish, y_fish, test_size=ratio)
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
        best_k = k
        best_ratio = 1 - ratio

print("Best Test Set Ratio:", ratio)
print("Best Training Set Ratio:", best_ratio)
print("Best K:", best_k)
print("Best Average Accuracy:", best_avg)
