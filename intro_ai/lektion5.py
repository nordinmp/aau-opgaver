import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score, KFold
import numpy as np
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.pipeline import make_pipeline


housing = pd.read_csv("datasets\housing.csv")
# Opret rooms_cat på hele DataFrame før split
 
print(len(housing)) 


print(housing.isnull().sum() )


num_features = housing.select_dtypes(include=[np.number]).columns

imputer_zero = SimpleImputer(strategy="constant", fill_value=0)
imputer_median = SimpleImputer(strategy="median")
imputer_mean = SimpleImputer(strategy="mean")


housing_zero = pd.DataFrame(imputer_zero.fit_transform(housing[num_features]), columns=num_features)
housing_median = pd.DataFrame(imputer_median.fit_transform(housing[num_features]), columns=num_features)
housing_mean = pd.DataFrame(imputer_mean.fit_transform(housing[num_features]), columns=num_features)

print(housing_median.isnull().sum())

knn_imputer = KNNImputer(n_neighbors=5)
housing_knn = pd.DataFrame(knn_imputer.fit_transform(housing[num_features]),

                           columns=num_features)

# print("Zero imputer:" + str(housing_zero.isnull().sum() ) )
# print("Median imputer:" + str(housing_median.isnull().sum() ) )
# print("Mean imputer:" + str(housing_mean.isnull().sum() ) )
# print("KNN imputer:" + str(housing_knn.isnull().sum() ) )

# housing_zero.hist(bins=50, figsize=(20,15))
# housing_median.hist(bins=50, figsize=(20,15))
# housing_mean.hist(bins=50, figsize=(20,15))

housing_knn.hist(bins=50, figsize=(20,15))
plt.show()

""" housing_data = housing.data[:, :2]  # Use only the first two features for visualization

housing_target = housing.target

X_train, X_test, y_train, y_test = train_test_split(housing, housing_target, test_size=0.3, random_state=42)


imputer = SimpleImputer(strategy="median")
X_train_imputed = pd.DataFrame(imputer.fit_transform(X_train[num_features]), columns=num_features)
X_test_imputed = pd.DataFrame(imputer.transform(X_test[num_features]), columns=num_features) """

print(housing["ocean_proximity"].value_counts())

housing["ocean_proximity"] = housing["ocean_proximity"].replace("Na", np.nan)

ordinal_encoder = OrdinalEncoder()
ordinal_encoder.fit_transform(housing[["ocean_proximity"]])

print(ordinal_encoder.categories_)

onehot_encoder = OneHotEncoder(sparse_output=False)
ocean_1hot = onehot_encoder.fit_transform(housing[["ocean_proximity"]])
ocean_1hot_df = pd.DataFrame(ocean_1hot, columns=onehot_encoder.get_feature_names_out(["ocean_proximity"]))

print(ocean_1hot_df.head())

standard_scaler = StandardScaler()
scaled_data = standard_scaler.fit_transform(housing[num_features])

scaled_df = pd.DataFrame(scaled_data, columns=housing[num_features].columns)

minmax_scaler = MinMaxScaler()
scaled_data_minmax = minmax_scaler.fit_transform(housing[num_features])
    
minmax_scaled_df = pd.DataFrame(scaled_data_minmax, columns=housing[num_features].columns)
# scaled_df.hist(bins=50, figsize=(20,15))

# minmax_scaled_df.hist(bins=50, figsize=(20,15))

housing.hist(bins=50, figsize=(20,15))

plt.show()

X = housing.select_dtypes(include=[np.number]).drop(columns=["median_house_value"])
y = housing["median_house_value"]

model = make_pipeline(SimpleImputer(strategy="median"), LinearRegression())
scores = cross_val_score(model, X, y, cv=10, scoring="r2")
print(f"Mean cross-validation score: {scores.mean():.4f}")
print(f"Standard deviation: {scores.std():.4f}")
