# Data Preprocessing Template

#Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing dataset
dataset = pd.read_csv('Data.csv')
#taking all rows exceot last column,matrix of features, independent variable
X = dataset.iloc[:,:-1].values
#Dependent variable
Y = dataset.iloc[:,3].values

