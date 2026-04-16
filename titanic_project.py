"""
Titanic Data Science Project
DevTown - Data Science With Python Bootcamp
Author: Ashish Cherian
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')
import os

os.makedirs('/home/claude/plots', exist_ok=True)

# =============================================================
# STEP 1: DATA COLLECTION
# =============================================================
print("=" * 60)
print("STEP 1: DATA COLLECTION")
print("=" * 60)

# Load the Titanic dataset from the CSV file in the workspace
df = pd.read_csv('titani.csv')
df.columns = df.columns.str.lower()
print(f"Dataset loaded successfully!")
print(f"Shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nColumn names: {list(df.columns)}")

# =============================================================
# STEP 2: DATA CLEANING & PREPROCESSING
# =============================================================
print("\n" + "=" * 60)
print("STEP 2: DATA CLEANING & PREPROCESSING")
print("=" * 60)

print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Fill missing 'age' with median
df['age'].fillna(df['age'].median(), inplace=True)

# Fill missing 'embarked' with mode
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

# Drop columns with too many missing values or irrelevant ones
df.drop(columns=['deck', 'embark_town', 'who', 'adult_male', 'alive', 'alone'], inplace=True, errors='ignore')

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Encode categorical variables
le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])         # male=1, female=0
df['embarked'] = le.fit_transform(df['embarked'].astype(str))

# =============================================================
# STEP 3: FEATURE ENGINEERING
# =============================================================
print("\n" + "=" * 60)
print("STEP 3: FEATURE ENGINEERING")
print("=" * 60)

# Create FamilySize feature
df['familysize'] = df['sibsp'] + df['parch'] + 1
print("Created 'familysize' = sibsp + parch + 1")
print(df[['sibsp', 'parch', 'familysize']].head())

# =============================================================
# STEP 4: DATA VISUALIZATION
# =============================================================
print("\n" + "=" * 60)
print("STEP 4: DATA VISUALIZATION")
print("=" * 60)

plt.style.use('seaborn-v0_8-whitegrid')

# --- Plot 1: Survival Count ---
fig, ax = plt.subplots(figsize=(7, 5))
sns.countplot(x='survived', data=df, palette=['#E74C3C', '#2ECC71'], ax=ax)
ax.set_title('Survival Count (0 = Did Not Survive, 1 = Survived)', fontsize=14, fontweight='bold')
ax.set_xlabel('Survived')
ax.set_ylabel('Count')
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=12)
plt.tight_layout()
plt.savefig('/home/claude/plots/01_survival_count.png', dpi=120)
plt.close()
print("Saved: 01_survival_count.png")

# --- Plot 2: Survival by Gender ---
fig, ax = plt.subplots(figsize=(7, 5))
sns.countplot(x='sex', hue='survived', data=df, palette=['#E74C3C', '#2ECC71'], ax=ax)
ax.set_title('Survival by Gender (0=Female, 1=Male)', fontsize=14, fontweight='bold')
ax.set_xlabel('Sex (0=Female, 1=Male)')
ax.set_ylabel('Count')
ax.legend(['Did Not Survive', 'Survived'])
plt.tight_layout()
plt.savefig('/home/claude/plots/02_survival_by_gender.png', dpi=120)
plt.close()
print("Saved: 02_survival_by_gender.png")

# --- Plot 3: Survival by Passenger Class ---
fig, ax = plt.subplots(figsize=(7, 5))
sns.countplot(x='pclass', hue='survived', data=df, palette=['#E74C3C', '#2ECC71'], ax=ax)
ax.set_title('Survival by Passenger Class', fontsize=14, fontweight='bold')
ax.set_xlabel('Passenger Class (1=First, 2=Second, 3=Third)')
ax.set_ylabel('Count')
ax.legend(['Did Not Survive', 'Survived'])
plt.tight_layout()
plt.savefig('/home/claude/plots/03_survival_by_class.png', dpi=120)
plt.close()
print("Saved: 03_survival_by_class.png")

# --- Plot 4: Age Distribution ---
fig, ax = plt.subplots(figsize=(8, 5))
df['age'].plot(kind='hist', bins=30, color='#3498DB', edgecolor='black', ax=ax)
ax.set_title('Age Distribution of Passengers', fontsize=14, fontweight='bold')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
plt.tight_layout()
plt.savefig('/home/claude/plots/04_age_distribution.png', dpi=120)
plt.close()
print("Saved: 04_age_distribution.png")

# --- Plot 5: Fare Distribution ---
fig, ax = plt.subplots(figsize=(8, 5))
df['fare'].plot(kind='hist', bins=40, color='#9B59B6', edgecolor='black', ax=ax)
ax.set_title('Fare Distribution', fontsize=14, fontweight='bold')
ax.set_xlabel('Fare (£)')
ax.set_ylabel('Frequency')
plt.tight_layout()
plt.savefig('/home/claude/plots/05_fare_distribution.png', dpi=120)
plt.close()
print("Saved: 05_fare_distribution.png")

# --- Plot 6: Correlation Heatmap ---
fig, ax = plt.subplots(figsize=(9, 7))
numeric_df = df.select_dtypes(include=[np.number])
corr = numeric_df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', mask=mask,
            square=True, linewidths=0.5, ax=ax, annot_kws={"size": 10})
ax.set_title('Feature Correlation Heatmap', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('/home/claude/plots/06_correlation_heatmap.png', dpi=120)
plt.close()
print("Saved: 06_correlation_heatmap.png")

# --- Plot 7: FamilySize vs Survival ---
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='familysize', y='survived', data=df, palette='viridis', ci=None, ax=ax)
ax.set_title('Survival Rate by Family Size', fontsize=14, fontweight='bold')
ax.set_xlabel('Family Size')
ax.set_ylabel('Survival Rate')
plt.tight_layout()
plt.savefig('/home/claude/plots/07_familysize_survival.png', dpi=120)
plt.close()
print("Saved: 07_familysize_survival.png")

# =============================================================
# STEP 5: MODEL BUILDING
# =============================================================
print("\n" + "=" * 60)
print("STEP 5: MODEL BUILDING - LOGISTIC REGRESSION")
print("=" * 60)

# Select features
features = ['pclass', 'sex', 'age', 'fare', 'familysize', 'embarked']
X = df[features]
y = df['survived']

# Drop any remaining NaNs
X = X.dropna()
y = y[X.index]

# Train-test split (80-20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\nTraining set size: {X_train.shape[0]}")
print(f"Test set size:     {X_test.shape[0]}")

# Train Logistic Regression
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# =============================================================
# STEP 6: EVALUATION
# =============================================================
print("\n" + "=" * 60)
print("STEP 6: MODEL EVALUATION")
print("=" * 60)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Did Not Survive', 'Survived']))

# Confusion Matrix Plot
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
            xticklabels=['Did Not Survive', 'Survived'],
            yticklabels=['Did Not Survive', 'Survived'],
            annot_kws={"size": 14})
ax.set_title('Confusion Matrix', fontsize=14, fontweight='bold')
ax.set_ylabel('Actual', fontsize=12)
ax.set_xlabel('Predicted', fontsize=12)
plt.tight_layout()
plt.savefig('/home/claude/plots/08_confusion_matrix.png', dpi=120)
plt.close()
print("Saved: 08_confusion_matrix.png")

# Feature Importance (Coefficients)
coef_df = pd.DataFrame({
    'Feature': features,
    'Coefficient': model.coef_[0]
}).sort_values('Coefficient', ascending=True)

fig, ax = plt.subplots(figsize=(8, 5))
colors = ['#E74C3C' if c < 0 else '#2ECC71' for c in coef_df['Coefficient']]
ax.barh(coef_df['Feature'], coef_df['Coefficient'], color=colors, edgecolor='black')
ax.set_title('Logistic Regression Feature Coefficients', fontsize=14, fontweight='bold')
ax.set_xlabel('Coefficient Value')
ax.axvline(0, color='black', linewidth=0.8)
plt.tight_layout()
plt.savefig('/home/claude/plots/09_feature_coefficients.png', dpi=120)
plt.close()
print("Saved: 09_feature_coefficients.png")

print("\n" + "=" * 60)
print("PROJECT COMPLETE!")
print(f"Final Model Accuracy: {accuracy * 100:.2f}%")
print("All plots saved to /home/claude/plots/")
print("=" * 60)
