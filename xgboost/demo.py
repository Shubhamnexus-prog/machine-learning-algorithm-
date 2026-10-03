import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
dataset = pd.read_csv(
    r"D:\ds 2\N_Batch -- 4.00PM -- Jun 26\3. Mar 26\7th -- REGRESSION PROJECT, POLY MODEL\poly\1.POLYNOMIAL REGRESSION\emp_sal.csv"
)

# Independent and dependent variables
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values



#xgboost

import xgboost as xg

xgb_r = xg.XGBRegressor(
    objective='reg:squarederror',
    n_estimators=4
)

xgb_r.fit(X, y)

xgb_reg_pred = xgb_r.predict([[6.5]])
print(xgb_reg_pred)



import xgboost as xg

xgb_r = xg.XGBRegressor(
        objective="reg:squarederror",
        n_estimators=100,
        learning_rate=0.1,
        max_depth=6,
        subsample=0.8,
        colsample_bytree=0.8,
        
    )
  


xgb_r.fit(X, y)

xgb_reg_pred = xgb_r.predict([[6.5]])
print(xgb_reg_pred)


