import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load the dataset
df = pd.read_csv('fake_profiles.csv')

# Step 2: Encode categorical features
label_encoder = LabelEncoder()
df['username'] = label_encoder.fit_transform(df['username'])

# Step 3: Define features and target
X = df.drop('label', axis=1)
y = df['label']

# Step 4: Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ✅ Save the scaler
joblib.dump(scaler, 'scaler.pkl')
print("✅ Scaler saved as scaler.pkl")

# Step 5: Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Step 6: Initialize models with tuned hyperparameters
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(max_depth=5),
    "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=5),
    "SVM": SVC(kernel='rbf', C=1.0, gamma='scale')
}

accuracies = {}

# Step 7: Train, Predict, and Evaluate each model
for name, model in models.items():
    print(f"\n----- {name} -----")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    accuracies[name] = accuracy  # Save accuracy
    
    print(f"Accuracy: {accuracy:.2f}")
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 8: Accuracy Comparison Graph
plt.figure(figsize=(8, 5))
plt.bar(accuracies.keys(), accuracies.values(), color='skyblue')
plt.title('Model Accuracy Comparison')
plt.ylabel('Accuracy')
plt.xlabel('Model')
plt.ylim(0, 1)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 9: Save the Best Model
best_model_name = max(accuracies, key=accuracies.get)
best_model = models[best_model_name]

joblib.dump(best_model, 'best_model.pkl')
print(f"\n✅ Best model saved: {best_model_name} (best_model.pkl)")