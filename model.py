import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import accuracy_score, confusion_matrix  

# 1. Load the dataset
df = pd.read_csv("data.csv")
print("\n Head of the dataset")
print(df.head())