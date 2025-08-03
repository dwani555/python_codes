import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Ignore non-critical warnings
warnings.filterwarnings("ignore")

# Set seaborn style
sns.set(style="whitegrid")

# -------------------------------
# 💎 Load Dataset
# -------------------------------
df = sns.load_dataset('diamonds')

# -------------------------------
# 🔍 Basic Dataset Exploration
# -------------------------------
print("🔍 First 5 Rows:")
print(df.head())

print("\nℹ️ Dataset Info:")
df.info()

print("\n📊 Summary Statistics:")
print(df.describe())

# -------------------------------
# 1️⃣ Price Distribution
# -------------------------------
plt.figure(figsize=(10, 5))
sns.histplot(df['price'], kde=True, color='skyblue')
plt.title('Distribution of Diamond Prices')
plt.xlabel('Price (USD)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# -------------------------------
# 2️⃣ Boxplot: Price vs Cut
# -------------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(x='cut', y='price', data=df, palette='Set2')
plt.title('Price vs Cut Quality')
plt.xlabel('Cut')
plt.ylabel('Price')
plt.tight_layout()
plt.show()

# -------------------------------
# 3️⃣ Boxplot: Price vs Clarity
# -------------------------------
plt.figure(figsize=(10, 5))
sns.boxplot(x='clarity', y='price', data=df, palette='Set3')
plt.title('Price vs Clarity')
plt.xlabel('Clarity')
plt.ylabel('Price')
plt.tight_layout()
plt.show()

# -------------------------------
# 4️⃣ Correlation Heatmap
# -------------------------------
plt.figure(figsize=(10, 7))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# -------------------------------
# 5️⃣ Pair Plot of Key Numerical Features
# -------------------------------
pairplot = sns.pairplot(df[['carat', 'price', 'depth', 'table']], corner=True)
pairplot.fig.suptitle('Pairwise Plots of Carat, Price, Depth, and Table', y=1.02)
plt.tight_layout()
plt.show()

# -------------------------------
# 6️⃣ Average Price by Color (Barplot)
# -------------------------------
plt.figure(figsize=(8, 5))
avg_price = df.groupby('color')['price'].mean().sort_index()
sns.barplot(x=avg_price.index, y=avg_price.values, palette='pastel')
plt.title('Average Price by Diamond Color')
plt.xlabel('Color Grade')
plt.ylabel('Average Price (USD)')
plt.tight_layout()
plt.show()

# -------------------------------
# 7️⃣ Price by Color and Clarity (Grouped Boxplot)
# -------------------------------
plt.figure(figsize=(12, 6))
sns.boxplot(x='color', y='price', hue='clarity', data=df)
plt.title('Price by Color and Clarity')
plt.xlabel('Color')
plt.ylabel('Price')
plt.legend(title='Clarity', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# -------------------------------
# 8️⃣ Scatter Plot: Carat vs Price (Colored by Cut)
# -------------------------------
plt.figure(figsize=(10, 6))
sns.scatterplot(x='carat', y='price', hue='cut', data=df, alpha=0.6)
plt.title('Price vs Carat Colored by Cut')
plt.xlabel('Carat')
plt.ylabel('Price')
plt.legend(title='Cut')
plt.tight_layout()
plt.show()