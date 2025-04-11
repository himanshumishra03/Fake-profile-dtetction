import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
num_real = 500
num_fake = 500

# Generate real profiles
real_profiles = {
    'username': ['user_real_' + str(i) for i in range(num_real)],
    'followers': np.random.randint(300, 10000, num_real),
    'following': np.random.randint(100, 3000, num_real),
    'posts': np.random.randint(50, 500, num_real),
    'bio_length': np.random.randint(50, 300, num_real),
    'label': [0] * num_real
}

# Generate fake profiles
fake_profiles = {
    'username': ['user_fake_' + str(i) for i in range(num_fake)],
    'followers': np.random.randint(0, 500, num_fake),
    'following': np.random.randint(500, 5000, num_fake),
    'posts': np.random.randint(0, 50, num_fake),
    'bio_length': np.random.randint(5, 100, num_fake),
    'label': [1] * num_fake
}

# Combine into one DataFrame
df_real = pd.DataFrame(real_profiles)
df_fake = pd.DataFrame(fake_profiles)
df = pd.concat([df_real, df_fake]).sample(frac=1).reset_index(drop=True)

# Save to CSV
df.to_csv('fake_profiles.csv', index=False)

print("✅ Dataset created successfully: fake_profiles.csv")
print(df.head())