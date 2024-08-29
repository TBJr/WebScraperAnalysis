import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_ecommerce_site():
    url = "https://amazon.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    products = []
    for item in soup.find_all("div", class_="product-item"):
        name = item.find("h2", class_="product-name").text.strip()
        price = item.find("span", class_="product-price").text.strip()
        reviews = item.find("div", class_="product-reviews").text.strip()

        products.append({
            "name": name,
            "price": price,
            "reviews": reviews
        })

    df = pd.DataFrame(products)
    df.to_csv("../data/raw_data.csv", index=False)

if __name__ == "__main__":
    scrape_ecommerce_site()