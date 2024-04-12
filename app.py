from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin
import re
import itertools
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def get_links(url):
    try:
        logging.info(f"Gathering Links in the Current page {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        links = set()
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and not ((href.startswith("#")) or ('/#' in href)):
                absolute_link = urljoin(url, href)
                parsed_link = urlparse(absolute_link)
                if parsed_link.scheme in ["http", "https"]:
                    links.add(absolute_link)
        return links
    except:
        logging.error(f"Error while gathering links in the current page")
        raise

def clean_links(links, base_url):
    logging.info(f"Cleaning External Links : {links}")
    try:
        cleaned = [ link for link in links if re.search(f'^{base_url}', link)]
        if base_url in cleaned:
            cleaned.remove(base_url)
        return cleaned
    except Exception as e:
        logging.error(f"Error while cleaning external links: {e}")
        raise

def create_sitemap(urls):
    sitemap = {}
    for url_parts in urls:
        current_level = sitemap
        for i, part in enumerate(url_parts):
            if i == len(url_parts) - 1:
                current_level.setdefault(part, {})
            else:
                current_level = current_level.setdefault(part, {})
    return sitemap

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            url = request.form["url"]
            x = get_links(url)
            y = clean_links(x, url)
            y = list(y)
            all_links = [y]
            for link in y:
                l = get_links(link)
                all_links.append(clean_links(l, link))
            all_links = list(itertools.chain(*all_links))
            unwanted = ['https:', 'http', '']
            cleaned_links = []
            for url in all_links:
                parts = url.split("/")
                parts = [i for i in parts if i not in unwanted]
                cleaned_links.append(parts)
            sitemap = create_sitemap(cleaned_links)
            return render_template("results.html", nested_dict=sitemap)

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return render_template("error.html", error=str(e))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

