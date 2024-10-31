import os
import requests
from urllib.parse import urlencode

EPIC_IMAGES_DIRECTORY = "./epic_images"

def build_epic_url(api_key):
    params = {'api_key': api_key}
    return 'https://api.nasa.gov/EPIC/api/natural/all?' + urlencode(params)

def fetch_epic_image_info(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def download_epic_images(count=1, api_key=None):
    if not os.path.exists(EPIC_IMAGES_DIRECTORY):
        os.makedirs(EPIC_IMAGES_DIRECTORY)

    url = build_epic_url(api_key)
    epic_image_info_list = fetch_epic_image_info(url)[:count]
    for item in epic_image_info_list:
        date_str = item['date'].split(' ')[0].replace('-', '/')
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date_str}/png/{item['image']}.png"
        print(f"EPIC Image URL: {image_url}")
        file_path = save_image(image_url, EPIC_IMAGES_DIRECTORY, f"epic_{date_str}")
        if file_path:
            print(f"Скачано изображение EPIC: {file_path}")

