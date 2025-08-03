import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import accuracy_score, confusion_matrix  


# Load the dataset
df = pd.read_csv("data.csv")

## SECTION 1: Cleaning the dataset
# Dropping the id column 
df.drop(columns=["Id"], inplace=True)
# Dropping the NaN / missing values
df.dropna(subset=['Bare.nuclei'], inplace=True)
# Changing data type for bare.nuclei
df['Bare.nuclei'] = df['Bare.nuclei'].astype(int)
# Renaming the columns for more clarity 
df.rename(columns={
    'Cl.thickness': 'Clump_Thickness',
    'Cell.size': 'Cell_Size_Uniformity',
    'Cell.shape': 'Cell_Shape_Uniformity',
    'Marg.adhesion': 'Marginal_Adhesion',
    'Epith.c.size': 'Epithelial_Cell_Size',
    'Bare.nuclei': 'Bare_Nuclei',
    'Bl.cromatin': 'Bland_Chromatin',
    'Normal.nucleoli': 'Normal_Nucleoli',
    'Mitoses': 'Mitoses',
    'Class': 'Diagnosis' 
}, inplace=True);

features = df.columns.difference(['Diagnosis'])  # exclude target column

plt.figure(figsize=(15, 10))
for i, col in enumerate(features, 1):
    plt.subplot(3, 3, i)
    sns.boxplot(y=df[col], color='skyblue')
    plt.title(col)
    plt.tight_layout()
plt.show()

#print(df.describe())
#print(df.info());

#print(f"\n Dataset shape: {df.shape} (rows, columns)")

#print(df.head())







































