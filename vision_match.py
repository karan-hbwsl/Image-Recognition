import os
import json
from google.cloud import vision

# Set up credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

client = vision.ImageAnnotatorClient()

# File to store cached labels
LABEL_CACHE_FILE = "labels.json"

# Load existing labels (if file exists)
def load_product_labels():
    if os.path.exists(LABEL_CACHE_FILE):
        with open(LABEL_CACHE_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_product_labels(product_labels):
    with open(LABEL_CACHE_FILE, "w") as f:
        json.dump(product_labels, f, indent=2)

# Label extractor function
def get_labels(image_path):
    with open(image_path, 'rb') as img_file:
        content = img_file.read()
    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    return [label.description for label in labels]

# Compare two label lists
def compare(label1, label2):
    return len(set(label1) & set(label2))  # common labels

# Function to update label cache for images in the images/ directory
def update_label_cache(product_dir="images"):
    product_labels = load_product_labels()
    updated = False
    for filename in os.listdir(product_dir):
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        if filename in product_labels:
            continue
        img_path = os.path.join(product_dir, filename)
        labels = get_labels(img_path)
        product_labels[filename] = labels
        updated = True
    if updated:
        save_product_labels(product_labels)
    return product_labels

# Main function to find top N matches for a test image
def find_top_matches(test_image_path, top_n=10, product_dir="images"):
    # Ensure label cache is up to date
    product_labels = update_label_cache(product_dir)
    test_labels = get_labels(test_image_path)
    scores = []
    for name, labels in product_labels.items():
        score = compare(test_labels, labels)
        scores.append((name, score))
    # Sort by score descending, then filename
    scores.sort(key=lambda x: (-x[1], x[0]))
    return scores[:top_n]

# If run as a script, do nothing (all logic is now in functions)
