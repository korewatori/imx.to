import argparse
import re
from bs4 import BeautifulSoup
import requests

# Regular expression to match imx.to album URLs
ALBUM_URL_REGEX = re.compile(r"https://imx.to/g/[a-zA-Z0-9]{4,}")

# Parse the command-line arguments using argparse
parser = argparse.ArgumentParser()
parser.add_argument("album_url", help="URL of the imx.to album")
args = parser.parse_args()

# Check if the URL is a valid imx.to album URL or not
if not ALBUM_URL_REGEX.match(args.album_url):
    print("Error: Invalid imx.to album URL")
    exit(1)

# Retrieve the contents of the webpage
response = requests.get(args.album_url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Create a set to store the URLs that we have already seen
seen_urls = set()

# Find all anchor tags
links = soup.find_all("a")

# Loop through the anchor tags and print the href attribute if it starts with "https://imx.to" and we haven't seen it before
for link in links:
    href = link["href"]
    if href.startswith("https://imx.to") and href not in seen_urls:
        print(href)
        seen_urls.add(href)