from scrapers.delhivery_scraper import DelhiveryScraper

def run_scrapers():
    print("Scraping Delhivery rates...")
    del_url = "https://www.delhivery.com/rate-calculator/"  # example only
    scraper = DelhiveryScraper(del_url)
    html = scraper.fetch_html()
    if html:
        data = scraper.parse(html)
        print(data)

if __name__ == "__main__":
    run_scrapers()
