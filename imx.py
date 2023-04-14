import argparse
import re
from bs4 import BeautifulSoup
import requests

# Regular expression to match imx.to album URLs
ALBUM_URL_REGEX = re.compile(r"https://imx.to/g/[a-zA-Z0-9]{4,}")

# Parse the command-line arguments using argparse
parser = argparse.ArgumentParser()
parser.add_argument("command", help="Action to perform (info or links)")
parser.add_argument("album_url", help="URL of the imx.to album")
parser.add_argument("-o", "--output", help="Path to the output file (optional)")
args = parser.parse_args()

if not ALBUM_URL_REGEX.match(args.album_url):
    print("Error: Invalid imx.to album URL")
    exit(1)

response = requests.get(args.album_url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

if args.command == "info":
    title_element = soup.select('.title')[0]
    title = title_element.text.strip()

    image_count_element = soup.select('.slider-wrapper > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)')[0]
    image_count = image_count_element.text

    file_size_element = soup.select('.slider-wrapper > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)')[0]
    file_size = file_size_element.text

    print(f'Title: {title}')
    print(f'Number of files: {image_count}')
    print(f'Size: {file_size}')
    print(f'URL: {args.album_url}')

elif args.command == "links":
    # Store the URLs that we have already seen in a set
    seen_urls = set()

    # Find all anchor tags
    links = soup.find_all("a")

    if args.output:
        with open(args.output, "w") as f:
            for link in links:
                href = link["href"]
                if href.startswith("https://imx.to") and href not in seen_urls:
                    f.write(href + "\n")
                    seen_urls.add(href)
    else:
        for link in links:
            href = link["href"]
            if href.startswith("https://imx.to") and href not in seen_urls:
                print(href)
                seen_urls.add(href)
