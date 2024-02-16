import json
import random


def send_random_img_url(json_file):
    json_file = 'gelbooru_img_urls.json'
    with open(json_file, 'r') as f:
        img_urls = json.load(f)

    # Pick a random URL from the list
    random_url = random.choice(img_urls)
    return random_url

if __name__ == "__main__":
    random_img_url = send_random_img_url('gelbooru_img_urls.json')
    print(random_img_url)
