#Simple Linear Regression

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

#Splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/4, random_state=0)

#Fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting the test set results
y_pred = regressor.predict(X_test)

#Visualising the training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Median home price vs interest rate (Training set)')
plt.xlabel('interest rate')
plt.ylabel('Median home price')
plt.show()

#Visualising the test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Median home price vs interest rate (Test set)')
plt.xlabel('interest rate')
plt.ylabel('Median home price')
plt.show()
