import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

dataset = pd.read_csv('dataset/Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

print("x")
print(x)
print("y")
print(y)

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(x[ : , 1:3])
x[ : , 1:3] = imputer.transform(x[ : , 1:3])

print("---------------------")
print("Handling the missing data")
print("x")
print(x)