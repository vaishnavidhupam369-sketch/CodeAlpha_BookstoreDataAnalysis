# CodeAlpha Bookstore Data Analysis

## Project Overview

This project was completed as part of my CodeAlpha Data Analytics Internship.

The project focuses on collecting, analyzing, and visualizing book data using Python.

## Tasks Completed

### Task 1 - Web Scraping

Book data was collected from Books to Scrape using:

- Python
- Requests
- BeautifulSoup
- Pandas

The dataset contains:

- Book Title
- Price
- Rating
- Availability
- URL

A total of 1,000 books were collected and saved as `books.csv`.

### Task 2 - Exploratory Data Analysis

Exploratory Data Analysis was performed using Pandas to understand the dataset.

The analysis included:

- Dataset structure
- Data types
- Missing values
- Summary statistics
- Rating distribution
- Availability
- Duplicate records
- Cheapest and most expensive books
- Average price and rating

### Task 3 - Data Visualization

Visualizations were created using Matplotlib and Seaborn.

The project includes:

- Rating Distribution
- Price Distribution
- Top 10 Most Expensive Books
- Price Distribution by Rating

## Key Findings

- The dataset contains 1,000 books.
- The average book price is approximately £35.07.
- The average rating is approximately 2.92 out of 5.
- All 1,000 books were listed as in stock.
- No duplicate rows were found.
- The cheapest book costs £10.00.
- The most expensive book costs £59.99.

## Technologies Used

- Python
- Pandas
- Requests
- BeautifulSoup
- Matplotlib
- Seaborn
- Google Colab
- GitHub

## Project Structure

```text
CodeAlpha_BookstoreDataAnalysis/
│
├── books.csv
├── task1_web_scraping.py
├── task2_eda.py
├── task3_visualization.py
│
└── visualizations/
    ├── rating_distribution.png
    ├── price_distribution.png
    ├── top_10_expensive_books.png
    └── rating_vs_price.png
