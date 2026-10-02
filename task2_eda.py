import pandas as pd

# Load dataset
df = pd.read_csv("books.csv")

print("===== DATASET OVERVIEW =====")
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))

print("\n===== DATA TYPES & MISSING VALUES =====")
print(df.info())

print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

print("\n===== RATING DISTRIBUTION =====")
print(df["Rating"].value_counts().sort_index())

print("\n===== AVAILABILITY =====")
print(df["Availability"].value_counts())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== CHEAPEST BOOK =====")
cheapest = df.loc[df["Price"].idxmin()]
print("Title:", cheapest["Title"])
print("Price:", cheapest["Price"])
print("Rating:", cheapest["Rating"])

print("\n===== MOST EXPENSIVE BOOK =====")
expensive = df.loc[df["Price"].idxmax()]
print("Title:", expensive["Title"])
print("Price:", expensive["Price"])
print("Rating:", expensive["Rating"])

print("\n===== AVERAGE PRICE =====")
print(df["Price"].mean())

print("\n===== AVERAGE RATING =====")
print(df["Rating"].mean())
