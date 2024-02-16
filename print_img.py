import json
import random


async def send_random_img_url(ctx, json_file):
    with open(json_file, 'r') as f:
        img_urls = json.load(f)

    # Pick a random URL from the list
    random_url = random.choice(img_urls)

    # Send the random URL to Discord
    await ctx.send(random_url)
