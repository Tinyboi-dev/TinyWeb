import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

visited = set()

def crawl(url, depth=2):
    if url in visited or depth == 0:
        return
    print(f"Crawling: {url}")
    visited.add(url)

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        os.makedirs("pages", exist_ok=True)
        with open(f"pages/{urlparse(url).netloc}_{len(visited)}.txt", "w", encoding='utf-8') as f:
            f.write(soup.get_text())

        for link in soup.find_all("a", href=True):
            new_url = urljoin(url, link["href"])
            if urlparse(new_url).netloc == urlparse(url).netloc:
                crawl(new_url, depth - 1)
    except:
        print(f"Failed: {url}")
