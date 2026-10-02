import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("books.csv")

# Create visualization folder
os.makedirs("visualizations", exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Rating Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Rating")
plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.savefig("visualizations/rating_distribution.png", bbox_inches="tight")
plt.show()
plt.close()

# 2. Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Price"], bins=20, kde=True)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.savefig("visualizations/price_distribution.png", bbox_inches="tight")
plt.show()
plt.close()

# 3. Top 10 Most Expensive Books
top_books = df.sort_values("Price", ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_books, x="Price", y="Title")
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.savefig("visualizations/top_10_expensive_books.png", bbox_inches="tight")
plt.show()
plt.close()

# 4. Price Distribution by Rating
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Rating", y="Price")
plt.title("Price Distribution by Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")
plt.savefig("visualizations/rating_vs_price.png", bbox_inches="tight")
plt.show()
plt.close()

print("All visualizations created successfully!")
