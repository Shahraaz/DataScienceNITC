# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

"""
#Taking care of missing Data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy='mean',axis = 0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

# Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X = LabelEncoder()
labelencoder_y = LabelEncoder()
onehotencoder = OneHotEncoder(categorical_features=[0])
X[:,0] = labelencoder_X.fit_transform(X[:,0])
X = onehotencoder.fit_transform(X).toarray()
y = labelencoder_y.fit_transform(y)
"""

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 1/3,random_state = 0)

# Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)

#Fitting Simple Linear Regression to Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

#Predicting the Test test results
y_pred = regressor.predict(X_test)

#Visualising the Training Set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train,regressor.predict(X_train),color = 'blue')
plt.title("Salary vs Experience (Trainging set)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()

#Visualising the Test Set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_test,regressor.predict(X_test),color = 'blue')
plt.title("Salary vs Experience (Test set)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()

