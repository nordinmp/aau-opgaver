import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
from pandas.plotting import scatter_matrix


""" def load_housing_data():
    return pd.read_csv("housing.csv")


housing = load_housing_data()
housing = housing.dropna()

# print(housing.info())
print(housing.describe())
# print(housing.head())

housing.hist(bins=50, figsize=(20,15))
plt.show()
 """

housing = pd.read_csv("datasets\housing.csv")
# Opret rooms_cat på hele DataFrame før split
housing["rooms_cat"] = pd.cut(housing["total_rooms"], bins=[0., 5000, 10000, np.inf], labels=[0, 1, 2])
test_size = 0.2
 
# Random split
train_set, test_set = train_test_split(housing, test_size=test_size, random_state=42)
# Stratified split (brug samme kolonne)
strat_train_set, strat_test_set = train_test_split(
    housing, test_size=test_size, stratify=housing["rooms_cat"], random_state=42)
 
""" print("Random split (test):")
print(test_set["rooms_cat"].value_counts(normalize=True))
 
print("Stratified split (test):")
print(strat_test_set["rooms_cat"].value_counts(normalize=True)) """
 
corr_matrix = housing.select_dtypes(include=[np.number]).corr()

plt.matshow(corr_matrix)

attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12, 8))

plt.show()