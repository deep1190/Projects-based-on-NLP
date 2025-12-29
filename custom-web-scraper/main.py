import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        sp = BeautifulSoup(html, "html.parser")
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url and "articles" in url:
                print(url)

website = "https://news.google.com/"
Scraper(website).scrape()
