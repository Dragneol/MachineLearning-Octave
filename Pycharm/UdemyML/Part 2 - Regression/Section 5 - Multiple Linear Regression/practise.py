# Multiple Linear Regression

# Import library
import numpy as np
import matplotlib
import pandas as pd
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Get Dataset
dataset = pd.read_csv('50_Startups.csv')

# Choose dependent and independent variables
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Encode Category Data
lbEncoder = LabelEncoder()
X[:, -1] = lbEncoder.fit_transform(X[:, -1])
onehotencoder = OneHotEncoder(categorical_features=[-1])
X = onehotencoder.fit_transform(X).toarray()

# Avoid the Dummy Variable Trap

# Slip train set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fitting Multiple Linear Regression to the Training Set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set result
y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination
X = np.append(arr=np.ones((50, 1)).astype(int), values=X, axis=1)
# X_opt =
