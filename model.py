import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import accuracy_score, confusion_matrix  

# explore.py

import pandas as pd

# Load the dataset
df = pd.read_csv("data.csv")  # Update with your actual file name/path if different

# Preview first few rows
print("\n🔹 Head of the dataset:")
print(df.head())

# Check shape of the dataset
print(f"\n🔹 Dataset shape: {df.shape} (rows, columns)")

# Column names
print("\n🔹 Column names:")
print(df.columns.tolist())

# Data types and non-null counts
print("\n🔹 Dataset info:")
print(df.info())

# Check for missing values
print("\n🔹 Missing values:")
print(df.isnull().sum())

# Basic statistics
print("\n🔹 Summary statistics:")
print(df.describe())

# Unique values in diagnosis
print("\n🔹 Class distribution (diagnosis):")
print(df["diagnosis"].value_counts())
