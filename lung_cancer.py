import pandas as pd

# Load your dataset
df = pd.read_csv("cleaned_lung_cancer_data.csv")

# Drop rows where all elements are NaN
# df.dropna(how='all', inplace=True)

# df['Patient_ID'] = range(1, len(df) + 1)

print(df.isnull().sum())

# Save the cleaned data
# df.to_csv("cleaned_lung_cancer_data.csv", index=False)

print("Patient ID column updated and file overwritten successfully!")
