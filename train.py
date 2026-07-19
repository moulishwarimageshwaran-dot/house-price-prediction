import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib

print("⏳ Machine Learning Model Training process start aagudhu...")

# 1. Dataset csv file-ah load pannuvom
try:
    df = pd.read_csv('datasets.csv')
except FileNotFoundError:
    print("❌ Error: 'datasets.csv' file illa! Mudhala fetch_data.py run pannunga.")
    exit()

# 2. X (Inputs / Features) matrum y (Output / Target Price) ah pirikkanum
X = df[['sqft', 'bedrooms', 'bathrooms', 'floors', 'age', 'parking', 'location_score', 'balcony', 'furnishing', 'location']]
y = df['price']

# 3. Data-va 80% Training matrum 20% Testing ku pirippom
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Linear Regression model-ah select panni train (fit) pannuvom
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Model evlavu accurate-ah predict pannudhu nu check pannuvom (R-squared score)
y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred) * 100
print(f"📊 Model Training Accuracy (R2 Score): {accuracy:.2f}%")

# 6. Train aana brain-ah (Model Object) 'model.pkl' file-ah save pannuvom
joblib.dump(model, 'model.pkl')
print("🔥 Successful! Unga model train aagi 'model.pkl' ah save aaiduchu.")
