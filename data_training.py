import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from data_prepare import data

# Define features and labels
features = data[['service', 'budget', 'payment_method', 'vip_service']]
labels = data['shop_index']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'shop_model.pkl')
