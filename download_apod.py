# download_apod.py
import requests
import os
from dotenv import load_dotenv
from general_functions import is_image_available, save_image
import argparse

load_dotenv()
APOD_IMAGES_DIRECTORY = './apod_images'

def fetch_apod_image_urls(api_key, count=5):
    """Получает URL изображений из Astronomy Picture of the Day."""
    endpoint = "/planetary/apod"
    params = {
        "api_key": api_key,
        "count": count
    }
    response = requests.get(f"https://api.nasa.gov{endpoint}", params=params)
    response.raise_for_status()
    apod_images_data = response.json()

    return [item['url'] for item in apod_images_data if item['media_type'] == 'image']

def download_apod_images(count=5):
    """Скачивает APOD изображения и сохраняет их в каталог."""
    api_key = os.getenv('NASA_API_KEY')
    apod_image_urls = fetch_apod_image_urls(api_key, count)
    for index, image_url in enumerate(apod_image_urls, start=1):
        save_image(image_url, APOD_IMAGES_DIRECTORY, f"apod_image_{index}.jpg")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Скачать изображения из APOD.')
    parser.add_argument('--count', type=int, default=5, help='Количество изображений для скачивания.')
    args = parser.parse_args()
    download_apod_images(args.count)