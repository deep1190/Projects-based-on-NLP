# Python Web Scraper for Google News

This project is a **Python web scraper** that extracts all the news article URLs from [Google News](https://news.google.com/). It uses **BeautifulSoup** to parse the HTML content and filter out article links.

---

## Features

- Fetches HTML content from Google News.
- Extracts all `<a>` tags containing article URLs.
- Filters URLs that contain the word `articles`.
- Prints all article links to the console.

---

## Requirements

- Python 3.x
- Libraries:
  - `beautifulsoup4`
  - `urllib` (built-in Python library)

Install BeautifulSoup using pip:

```bash
pip install beautifulsoup4
