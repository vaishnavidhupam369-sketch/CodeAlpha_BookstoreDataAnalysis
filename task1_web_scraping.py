import requests
from bs4 import BeautifulSoup
import pandas as pd

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

books_data = []

for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]

        price_text = book.find(
            "p", class_="price_color"
        ).text.strip()

        price = float(
            price_text.replace("£", "").replace("Â", "")
        )

        rating_text = book.find(
            "p", class_="star-rating"
        )["class"][1]

        rating = rating_map[rating_text]

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        relative_url = book.h3.a["href"]

        book_url = (
            "https://books.toscrape.com/catalogue/"
            + relative_url.replace("../", "")
        )

        books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "URL": book_url
        })

df = pd.DataFrame(books_data)

df.to_csv("books.csv", index=False)

print("Total books scraped:", len(df))
print("Data saved as books.csv")
