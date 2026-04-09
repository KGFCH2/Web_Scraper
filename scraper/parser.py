from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")

    data = {
        "title": soup.title.string if soup.title else "",
        "headings": [h.text.strip() for h in soup.find_all(["h1","h2","h3"])],
        "links": [a.get("href") for a in soup.find_all("a")],
        "images": [img.get("src") for img in soup.find_all("img")],
        "paragraphs": [p.text.strip() for p in soup.find_all("p")]
    }

    return data