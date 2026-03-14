import numpy as np
from sklearn.cluster import KMeans

print("Customer Segmentation System")
print("-----------------------------")

# Training dataset
data = np.array([
    [19, 15, 39],
    [21, 16, 81],
    [20, 17, 6],
    [23, 18, 77],
    [31, 40, 40],
    [22, 42, 76],
    [35, 60, 6],
    [40, 65, 94],
    [45, 70, 3],
    [50, 80, 72]
])

# Train model
model = KMeans(n_clusters=3, random_state=0)
model.fit(data)

# User input
age = int(input("Enter customer age: "))
income = int(input("Enter annual income: "))
spending = int(input("Enter spending score (1-100): "))

customer = [[age, income, spending]]

group = model.predict(customer)

print("-----------------------------")

if group[0] == 0:
    print("Customer Group: Budget Customers")
elif group[0] == 1:
    print("Customer Group: Regular Customers")
else:
    print("Customer Group: Premium Customers")

print("-----------------------------")