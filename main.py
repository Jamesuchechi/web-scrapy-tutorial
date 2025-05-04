import requests
from bs4 import BeautifulSoup
import csv


url = "http://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h3")
for title in titles:
    print(title.text.strip())

url = "http://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")
for book in books:
    title = book.find('h3').text.strip()
    price = book.find('p', class_='price_color').text.strip()
    print(f"Title: {title}, Price: {price}")

with open("books.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Price"])
    for book in books:
        title = book.find('h3').text.strip()
        price = book.find('p', class_='price_color').text.strip()
        writer.writerow([title, price])