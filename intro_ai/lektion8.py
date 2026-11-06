import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics


titanicData = pd.read_csv("datasets/titanic.csv")

titanicData["Sex"] = titanicData["Sex"].map({"male": 0, "female": 1})

X = titanicData[["Pclass", "Sex", "Age", "SibSp", "Parch"]].values
y = titanicData[["Survived"]].values


x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=10, random_state=42, min_samples_leaf=5)
model.fit(x_train, y_train)

accuracy = model.score(x_test, y_test)

print(accuracy)

model = RandomForestClassifier(n_estimators=50, random_state=42, min_samples_leaf=3)
model.fit(x_train, y_train)

accuracy = model.score(x_test, y_test)

print(accuracy)

