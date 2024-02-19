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

import json
import os

def add_praise():
    # Check if counter.json exists
    if not os.path.exists('counter.json'):
        with open('counter.json', 'w') as f:
            json.dump({'praise_count': 0, 'fail_count': 0}, f)

    # Increment praise_count by 1
    with open('counter.json', 'r+') as f:
        data = json.load(f)
        data['praise_count'] += 1
        f.seek(0)
        json.dump(data, f)

def add_fail():
    # Check if counter.json exists
    if not os.path.exists('counter.json'):
        with open('counter.json', 'w') as f:
            json.dump({'praise_count': 0, 'fail_count': 0}, f)

    # Increment fail_count by 1
    with open('counter.json', 'r+') as f:
        data = json.load(f)
        data['fail_count'] += 1
        f.seek(0)
        json.dump(data, f)

def count_score():
    # Check if counter.json exists
    if not os.path.exists('counter.json'):
        return "Praise Count: 0\nFail Count: 0"

    # Read praise_count and fail_count from counter.json
    with open('counter.json', 'r') as f:
        data = json.load(f)
        praise_count = data.get('praise_count', 0)
        fail_count = data.get('fail_count', 0)

    # Format the counts into a string
    return f"Praise Count: {praise_count}\nFail Count: {fail_count}"