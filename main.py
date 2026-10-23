import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Ensure assets directory exists for saving plots
os.makedirs("assets", exist_ok=True)

# 1. Load Data
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("--- Initial Inspection ---")
print(df.info())
print("\n--- Summary Statistics ---")
print(df.describe())

# 2. Data Cleaning & Handling Missing Values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df = df.drop_duplicates()

# 3. Filtering Example: First-Class Passengers
first_class = df[df["Pclass"] == 1]
print(f"\nTotal First-Class Passengers: {len(first_class)}")
print(first_class.head())

# -------------------------------------------------------------
# Visualizations & Asset Generation
# -------------------------------------------------------------

# Plot 1: Survival Rate by Passenger Class
plt.figure(figsize=(6, 4))
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("assets/survival_by_class.png", dpi=300)
plt.show()

# Plot 2: Age Distribution
plt.figure(figsize=(7, 4))
sns.histplot(df["Age"], kde=True, bins=20, color="purple")
plt.title("Passenger Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("assets/age_distribution.png", dpi=300)
plt.show()

# Plot 3: Scatter Plot - Age vs. Fare
plt.figure(figsize=(7, 4))
plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="green")
plt.title("Age vs. Ticket Fare")
plt.xlabel("Age")
plt.ylabel("Fare (£)")
plt.tight_layout()
plt.savefig("assets/age_vs_fare.png", dpi=300)
plt.show()

print("\nEDA processing complete. Generated plots saved to 'assets/' folder.")