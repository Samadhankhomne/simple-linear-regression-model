import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\91976\Downloads\Salary_Data.csv")

#check the shape of the dataset
print("Data shape: ",df.shape)

#Feature selection (independent variable X and dependent variable Y)
x = df.iloc[:,:-1] # years of experience (Independent variable)
y = df.iloc[:,-1]  #Salary (Dependent variable)

# Split the dataset into training and testing sets(80% training, testing 20%)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.20, random_state=0)

# Reshape x_train and y_test into 2D arrays if they are single feature columns
x_train = x_train.values.reshape(-1,1)
x_test = x_test.values.reshape(-1,1)

# you don't need to reshape y_train, as it's the target variable
# Fit the Linear regreession model to the training set
from sklearn.linear_model import LinearRegression
regressor  = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting the results for the test set
y_pred = regressor.predict(x_test)

# Visualizing the Training set results
plt.scatter(x_train, y_train, color = 'red')  # Real salary data (training)
plt.plot(x_train, regressor.predict(x_train), color = 'blue')  # Predicted regression line
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualizing the Test set results
plt.scatter(x_test, y_test, color = 'red')  # Real salary data (testing)
plt.plot(x_train, regressor.predict(x_train), color = 'blue')  # Regression line from training set
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Optional: Output the coefficients of the linear model
print(f"Intercept: {regressor.intercept_}")
print(f"Coefficient: {regressor.coef_}")


# Compare predicted and actual salaries from the test set
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)