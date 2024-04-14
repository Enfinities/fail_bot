import requests
from bs4 import BeautifulSoup
import json


def extract_sample_sizes(urls):
    sample_sizes = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            # Find all span tags with class "thumb"
            thumb_spans = soup.find_all('span', class_='thumb')
            # Extract sample sizes from thumb spans and append to sample_sizes list
            for span in thumb_spans:
                # Sample size is usually provided as the title attribute of the span
                sample_size = span.get('title')
                if sample_size:
                    sample_sizes.append(sample_size)
    return sample_sizes


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

# Extract sample sizes from the provided Gelbooru URLs
sample_sizes = extract_sample_sizes(urls)

# Write sample_sizes to a JSON file
with open('gelbooru_sample_sizes.json', 'w') as f:
    json.dump(sample_sizes, f, indent=4)

# Example usage:
print("Sample sizes extracted and saved to gelbooru_sample_sizes.json")