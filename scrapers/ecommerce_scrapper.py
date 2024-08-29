import os

import pandas as pd
import requests
from bs4 import BeautifulSoup

# def scrape_ecommerce_site():
#     url = "https://example-ecommerce.com/products"  # Replace with a valid URL
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     products = []
#     for item in soup.find_all("div", class_="product-item"):  # Adjust class names as needed
#         name = item.find("h2", class_="product-name").text.strip()  # Adjust class names as needed
#         price = item.find("span", class_="product-price").text.strip()  # Adjust class names as needed
#         reviews = item.find("div", class_="product-reviews").text.strip()  # Adjust class names as needed
#
#         products.append({
#             "name": name,
#             "price": price,
#             "reviews": reviews
#         })
#
#     df = pd.DataFrame(products)
#
#     # Define the directory path
#     data_directory = './data'
#
#     # Create the directory if it doesn't exit
#     if not os.path.exists(data_directory):
#         os.makedirs(data_directory)
#
#     # Now proceed with saving the file
#     df.to_csv(os.path.join(data_directory, 'raw_data.csv'), index=False)
#
# if __name__ == "__main__":
#     scrape_ecommerce_site()
#

def scrape_books():
    url = "http://books.toscrape.com/catalogue/page-1.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    books = []
    for item in soup.find_all("article", class_="product_pod"):
        # Extract the book title
        title = item.find("h3").find("a")["title"].strip()

        # Extract the price
        price = item.find("p", class_="price_color").text.strip()

        # Extract the availability
        availability = item.find("p", class_="instock availability").text.strip()

        books.append({
            "title": title,
            "price": price,
            "availability": availability
        })

    # Check if data is being collected
    print(f"Scraped {len(books)} books.")

    df = pd.DataFrame(books)

    # Define the directory path
    data_directory = './data'

    # Create the directory if it doesn't exist
    if not os.path.exists(data_directory):
        print(f"Creating directory: {data_directory}")
        os.makedirs(data_directory)

    # Define the full file path
    file_path = os.path.join(data_directory, 'books.csv')

    # Save the DataFrame to a CSV file
    print(f"Saving data to {file_path}")
    df.to_csv(file_path, index=False)

    # Confirm the file creation
    if os.path.exists(file_path):
        print(f"File {file_path} created successfully.")
    else:
        print(f"Failed to create file {file_path}.")

if __name__ == "__main__":
    scrape_books()