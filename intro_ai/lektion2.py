# introduktion til ai


## Test 1:
""" import sys
import pandas as pd
import sklearn as sk
import matplotlib as mpl


print(f"Python version: {sys.version}")
print(f"Pandas version: {pd.__version__}")
print(f"Scikit-learn version: {sk.__version__}")
print(f"Matplotlib version: {mpl.__version__}") """


# print mean hsv værdi -> gem i csv fil, træn scikit model, test på andre billeder hvor man få mean hsv værdi

# tegn på en graf, af vores træningsdata, for at se hvor de ligger på en graf (og kan det kategoriseres for hvert terraintype)


# Test 2
import sklearn as sk
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
    
iris = datasets.load_iris()

# Clean up code
iris_data = iris.data[:, :2]  # Use only the first two features for visualization
print(iris_data)

iris_target = iris.target
print(iris_target)

X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_target, test_size=0.3, random_state=42)

k = 5
knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of KNN classifier with k={k}: {accuracy * 100:.2f}%")
