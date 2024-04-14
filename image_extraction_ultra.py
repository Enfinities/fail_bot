import json

def transform_urls(input_file, output_file):
    # Read URLs from input JSON file
    with open(input_file, 'r') as f:
        img_urls = json.load(f)

    # Transform each URL
    transformed_urls = []
    for url in img_urls:
        # Replace "thumbnails" with "samples" and remove "thumbnail_" from the filename
        transformed_url = url.replace("thumbnails", "/samples").replace("thumbnail_", "sample_")
        transformed_urls.append(transformed_url)

    # Write transformed URLs to output JSON file
    with open(output_file, 'w') as f:
        json.dump(transformed_urls, f, indent=4)

# Example usage:
transform_urls("gelbooru_img_urls.json", "transformed_img_urls.json")
print("URLs transformed and saved to transformed_img_urls.json")