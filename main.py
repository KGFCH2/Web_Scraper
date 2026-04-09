from scraper.fetcher import fetch_static, fetch_dynamic, fetch_static_screenshot
from scraper.parser import parse_html
from scraper.exporter import export_excel, export_json, export_pdf, export_txt, export_html, export_screenshot

def scrape(url, dynamic=False, username=None, password=None):
    html = fetch_dynamic(url, username, password) if dynamic else fetch_static(url)

    if not html:
        print("Failed to fetch page")
        return
    
    # For static pages, capture screenshot separately
    if not dynamic:
        fetch_static_screenshot(url)

    data = parse_html(html)

    export_excel(data)
    export_json(data)
    export_pdf(data)
    export_txt(data)
    export_html(data, html)
    export_screenshot()

    print("Scraping completed! Check output folder.")

if __name__ == "__main__":
    url = input("Enter URL: ")
    mode = input("Dynamic? (y/n): ")
    dynamic = mode.lower() == "y"
    
    username = None
    password = None
    if dynamic:
        auth = input("Need authentication? (y/n): ")
        if auth.lower() == "y":
            username = input("Username: ")
            password = input("Password: ")

    scrape(url, dynamic, username, password)
