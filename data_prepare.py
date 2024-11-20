import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample Shops data
shops = [
    {"name": "Occasion Technology Shop", "price_min": 1200, "price_max": 5000},
    {"name": "ElectroHub", "price_min": 2000, "price_max": 15000},
    {"name": "TechMart", "price_min": 3000, "price_max": 20000}
]

# Convert shops data to DataFrame
data = pd.DataFrame(shops)

# Create dummy features and labels
data['service'] = [0, 1, 1]  # Dummy service feature
data['budget'] = [2000, 10000, 5000]  # User budget
data['payment_method'] = [0, 1, 0]  # Dummy payment method feature
data['vip_service'] = [1, 0, 1]  # Dummy VIP service feature

# Label the shop index (this is what to predict)
data['shop_index'] = data.index
