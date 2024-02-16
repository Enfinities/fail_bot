import requests
from bs4 import BeautifulSoup
import json

def extract_img_urls(urls):
    img_urls = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            # Find all img tags with src attribute
            img_tags = soup.find_all('img', src=True)
            # Extract src attribute value and append to img_urls list
            img_urls.extend([img['src'] for img in img_tags])
    return img_urls

# List of Gelbooru URLs to scrape
urls = [
    "https://gelbooru.com/index.php?page=post&s=list&tags=makinaru&pid=0",
    "https://gelbooru.com/index.php?page=post&s=list&tags=makinaru&pid=42",
    "https://gelbooru.com/index.php?page=post&s=list&tags=makinaru&pid=84",
    "https://gelbooru.com/index.php?page=post&s=list&tags=makinaru&pid=126",
    "https://gelbooru.com/index.php?page=post&s=list&tags=makinaru&pid=168",
    "https://gelbooru.com/index.php?page=post&s=list&tags=makinaru&pid=210",
    "https://gelbooru.com/index.php?page=post&s=list&tags=makinaru&pid=252"
]

# Extract img src links from the provided Gelbooru URLs
img_urls = extract_img_urls(urls)

# Write img_urls to a JSON file
with open('gelbooru_img_urls.json', 'w') as f:
    json.dump(img_urls, f)

print("Image URLs extracted and saved to gelbooru_img_urls.json")