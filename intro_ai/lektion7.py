import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression, LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics


#opgave 1
""" CO2_df = pd.read_csv("datasets/CO2data.csv")


X = CO2_df[["Weight", "Volume"]].values
y = CO2_df["CO2"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#create 3d scatter plot
#fig = plt.figure(figsize=(10, 8))
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(X["Weight"], X["Volume"], y)

#plt.show()

model = LinearRegression()

model.fit(X_train, y_train)

bias = model.intercept_
weights = model.coef_

print(f"Bias: {bias}")
print(f"Weights: {weights}")

x_new = [[2300, 1300]]

y_pred = model.predict(x_new)

print(f"Predicted CO2 emission for a car with weight {x_new[0][0]} kg and volume {x_new[0][1]} cm^3: {y_pred[0]:.2f} g/km")

# calculate R^2 score and mean squared error
r2_score = model.score(X_test, y_test)
test_predictions = model.predict(X_test)
mse = metrics.mean_squared_error(y_test, test_predictions)


print(f"R^2 Score: {r2_score}")
print(f"Mean Squared Error: {mse}")

#visualize the regression line in 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], y)

weight_grid, volume_grid = np.meshgrid(
	np.linspace(X[:, 0].min(), X[:, 0].max(), 30),
	np.linspace(X[:, 1].min(), X[:, 1].max(), 30),
)
grid_points = np.column_stack((weight_grid.ravel(), volume_grid.ravel()))
co2_grid = model.predict(grid_points).reshape(weight_grid.shape)
ax.plot_surface(weight_grid, volume_grid, co2_grid, alpha=0.5, cmap="viridis")

ax.set_xlabel("Weight")
ax.set_ylabel("Volume")
ax.set_zlabel("CO2")

plt.show()
 """

# Opgave 2

CVDdata = pd.read_csv("datasets/CVDdata.csv")

X = CVDdata[["BP", "Smoking"]].values
y = CVDdata["CVD"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(X_train, y_train)

x_new = [[145, 0]]

y_pred = model.predict(x_new)

y_proba = model.predict_proba(x_new)[:, 1]

print(f"Predicted CVD risk for a person with BP {x_new[0][0]} and Smoking status {x_new[0][1]}: {y_pred[0]}")
print(f"Probability of CVD for the same person: {y_proba[0]:.2f}")

# Visualize the sigmoid curve
bp_values = np.linspace(X[:, 0].min(), X[:, 0].max(), 200)

plt.figure(figsize=(8, 5))
for smoking_status in (0, 1):
	curve_points = np.column_stack((bp_values, np.full_like(bp_values, smoking_status)))
	plt.plot(bp_values, model.predict_proba(curve_points)[:, 1], label=f"Smoking = {smoking_status}")

plt.xlabel("Blood pressure (BP)")
plt.ylabel("Predicted probability of CVD")
plt.title("CVD probability by blood pressure and smoking status")
plt.ylim(0, 1)
plt.legend()
plt.grid(True)
plt.show()


test_proba = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = metrics.roc_curve(y_test, test_proba)
roc_auc = metrics.auc(fpr, tpr)
display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc,
                                  name='example estimator')
display.plot()
plt.show()