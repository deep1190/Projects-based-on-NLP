# Web Scraping to Create CSV - Flipkart Mobile Data

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

# URL to scrape
my_url = "https://www.flipkart.com/search?q=samsung+mobiles"

# Open connection and read page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# Parse HTML
page_soup = soup(page_html, "html.parser")

# Find all product containers
containers = page_soup.findAll("div", {"class": "_3O0U0u"})

# CSV file setup
filename = "products.csv"
f = open(filename, "w", newline="", encoding='utf-8')
headers = ["Product_Name", "Price", "Ratings"]
writer = csv.writer(f)
writer.writerow(headers)

# Extract product details and write to CSV
for container in containers:
    product_name = container.div.img["alt"]
    
    price_container = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()
    
    rating_container = container.findAll("div", {"class": "niH0FQ"})
    rating = rating_container[0].text
    
    writer.writerow([product_name, price, rating])
    print(f"Product_Name: {product_name}, Price: {price}, Ratings: {rating}")

f.close()
print("Data scraped and saved to products.csv successfully!")
