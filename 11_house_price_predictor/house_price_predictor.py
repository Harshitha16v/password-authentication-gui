import numpy as np
from sklearn.linear_model import LinearRegression
# Training dataset
sizes = np.array([600, 800, 1000, 1200, 1500]).reshape(-1, 1)
prices = np.array([30, 40, 50, 60, 75])
# Train the model
model = LinearRegression()
model.fit(sizes, prices)
print("House Price Prediction System")
print("--------------------------------")
# User input
size = float(input("Enter house size in square feet: "))
# Prediction
predicted_price = model.predict([[size]])
print("--------------------------------")
print(f"Estimated House Price: {predicted_price[0]:.2f} Lakhs")
print("--------------------------------")
