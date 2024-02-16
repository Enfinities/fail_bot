import json
import random

json_file = 'gelbooru_img_urls.json'
def send_random_img_url(json_file):
    with open(json_file, 'r') as f:
        img_urls = json.load(f)

    # Pick a random URL from the list
    random_url = random.choice(img_urls)
    return random_url

if __name__ == "__main__":
    random_img_url = send_random_img_url(json_file)
    print(random_img_url)
