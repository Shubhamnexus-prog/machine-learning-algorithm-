# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:14:47 2026

@author: SHUBHAM
"""

import pandas as pd
import numpy as np

#Import graphical plotting libraries
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline

#Import Linear Regression Machine Learning Libraries
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score

dataset=pd.read_csv(r'D:\ds 2\N_Batch -- 4.00PM -- Jun 26\3. Mar 26\6th- l1, l2, scaling\lasso, ridge, elastic net\TASK-22_LASSO,RIDGE/car-mpg.csv')
dataset.head()