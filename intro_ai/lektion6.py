import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split, cross_val_score
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

breast_cancer_df = pd.read_csv("datasets/breast-cancer.csv")
 
breast_cancer_df["diagnosis"] = breast_cancer_df["diagnosis"].map({"M": 1, "B": 0})

colors = breast_cancer_df["diagnosis"].map({0: "blue", 1: "red"})

attributes = ["radius_mean", "texture_mean", "perimeter_mean", "area_mean"]

scatter_matrix(
    breast_cancer_df[attributes],
    figsize=(12, 8),
    c=colors,
)
## plt.show()

X = breast_cancer_df.drop(columns=["id", "diagnosis"])
# Clean up code
X = X[attributes]
y = breast_cancer_df["diagnosis"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()

print(X.shape, y.value_counts())

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)


y_proba = model.predict_proba(X_test_scaled)[:, 1]
threshold = 0.5
y_pred_t = (y_proba >= threshold).astype(int)

cm = confusion_matrix(y_test, y_pred_t)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Blues")

plt.show()

accuracy = accuracy_score(y_test, y_pred_t)

precision = precision_score(y_test, y_pred_t)

recall = recall_score(y_test, y_pred_t)

tn, fp, fn, tp = cm.ravel()

specificity = tn / (tn+fp)

npv = tn / (tn+fn)

f1 = f1_score(y_test, y_pred_t)
print(accuracy, precision, recall, specificity, npv, f1)


fpr, tpr, thresholds = metrics.roc_curve(y_test, y_proba)
roc_auc = metrics.auc(fpr, tpr)
display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc,
                                  name='example estimator')
display.plot()
plt.show()

