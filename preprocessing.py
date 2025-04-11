import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Step 1: Load the dataset
df = pd.read_csv('fake_profiles.csv')

print("First 5 rows of the dataset:")
print(df.head())

# Step 2: Check for missing values
print("\nChecking for missing values:")
print(df.isnull().sum())

# Step 3: Encode the label column (if not already numeric)
# In our dataset, label is already 0/1 — skip if so, otherwise:
if df['label'].dtype == 'object':
    label_encoder = LabelEncoder()
    df['label'] = label_encoder.fit_transform(df['label'])

# Step 4: Define features and target
X = df.drop('label', axis=1)  # Features (input)
y = df['label']              # Target (output)

# Step 5: Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 6: Print the shapes of the splits
print("\nTraining set size:", X_train.shape)
print("Test set size:", X_test.shape)

# Optional: Save the split datasets if you want to use them later
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)

print("\nPreprocessing complete! Training and test data saved.")