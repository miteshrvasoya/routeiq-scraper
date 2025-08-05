import requests
from bs4 import BeautifulSoup
from config import HEADERS

class BaseScraper:
    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        try:
            response = requests.get(self.url, headers=HEADERS)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Error: {response.status_code}")
        except Exception as e:
            print("Failed to fetch data:", str(e))
        return None

    def parse(self, html):
        raise NotImplementedError("Subclasses must override this method")
