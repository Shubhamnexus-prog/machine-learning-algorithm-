import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

# ======================================
# Load Dataset
# ======================================

dataset = pd.read_csv(
    r"C:\Users\SHUBHAM\Downloads\7th- l1, l2, scaling\7th- l1, l2, scaling\lasso, ridge, elastic net\TASK-22_LASSO,RIDGE\car-mpg.csv",
    na_values='?'
)

# Remove extra spaces from column names
dataset.columns = dataset.columns.str.strip()

print("Columns:")
print(dataset.columns.tolist())

# ======================================
# Handle Missing Values
# ======================================

# Convert hp column to numeric
dataset["hp"] = pd.to_numeric(dataset["hp"], errors="coerce")

# Fill missing values with mean
dataset["hp"] = dataset["hp"].fillna(dataset["hp"].mean())

# ======================================
# Features and Target
# ======================================

X = dataset.drop("mpg", axis=1)
y = dataset["mpg"]

# Remove all string/object columns (like car name)
X = X.select_dtypes(exclude=["object"])

print("\nFeatures Used:")
print(X.columns.tolist())

print("\nDataset Info")
print(dataset.info())

# ======================================
# Train-Test Split
# ======================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ======================================
# Linear Regression
# ======================================

linear = LinearRegression()
linear.fit(X_train, y_train)

y_pred_linear = linear.predict(X_test)

print("\n========== Linear Regression ==========")
print("R2 Score :", round(r2_score(y_test, y_pred_linear), 4))
print("MSE      :", round(mean_squared_error(y_test, y_pred_linear), 4))

# ======================================
# Ridge Regression
# ======================================

ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

y_pred_ridge = ridge.predict(X_test)

print("\n========== Ridge Regression ==========")
print("R2 Score :", round(r2_score(y_test, y_pred_ridge), 4))
print("MSE      :", round(mean_squared_error(y_test, y_pred_ridge), 4))

# ======================================
# Lasso Regression
# ======================================

lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

y_pred_lasso = lasso.predict(X_test)

print("\n========== Lasso Regression ==========")
print("R2 Score :", round(r2_score(y_test, y_pred_lasso), 4))
print("MSE      :", round(mean_squared_error(y_test, y_pred_lasso), 4))

# ======================================
# Model Coefficients
# ======================================

coef = pd.DataFrame({
    "Feature": X.columns,
    "Linear": linear.coef_,
    "Ridge": ridge.coef_,
    "Lasso": lasso.coef_
})

print("\nModel Coefficients")
print(coef)

# ======================================
# Plot 1 : Coefficient Comparison
# ======================================

plt.figure(figsize=(12,6))

plt.plot(coef["Feature"], coef["Linear"],
         marker='o', linewidth=2, label="Linear")

plt.plot(coef["Feature"], coef["Ridge"],
         marker='s', linewidth=2, label="Ridge")

plt.plot(coef["Feature"], coef["Lasso"],
         marker='^', linewidth=2, label="Lasso")

plt.xticks(rotation=45)
plt.xlabel("Features")
plt.ylabel("Coefficient")
plt.title("Coefficient Comparison")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ======================================
# Plot 2 : Actual vs Predicted
# ======================================

plt.figure(figsize=(8,6))

plt.scatter(y_test, y_pred_linear,
            color="blue", label="Linear")

plt.scatter(y_test, y_pred_ridge,
            color="green", label="Ridge")

plt.scatter(y_test, y_pred_lasso,
            color="red", label="Lasso")

# Perfect prediction line
min_val = min(y_test.min(), y_pred_linear.min())
max_val = max(y_test.max(), y_pred_linear.max())

_val, max_val],
         [min_val, max_val],
         color="black",
         linestyle="--",
         label="Perfect Prediction")

plt.xlabel("Actual MPG")
plt.ylabel("Predicted MPG")
plt.title("Actual vs Predicted MPG")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ======================================
# Plot 3 : Residual Plot
# ======================================

plt.figure(figsize=(8,6))

residuals = y_test - y_pred_linear

plt.scatter(y_pred_linear, residuals, color='purple')
plt.axhline(y=0, color='red', linestyle='--')

plt.xlabel("Predicted MPG")
plt.ylabel("Residuals")
plt.title("Residual Plot (Linear Regression)")
plt.grid(True)

plt.show()



      




















