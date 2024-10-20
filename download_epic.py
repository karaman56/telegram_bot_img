# download_epic.py
import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from general_functions import is_image_available, save_image
import argparse

load_dotenv()
EPIC_IMAGES_DIRECTORY = './epic_images'

def fetch_epic_image_urls(api_key, count=5):
    """Получает URL изображений Земли из EPIC."""
    endpoint = "/EPIC/api/natural/images"
    params = {
        "api_key": api_key
    }
    response = requests.get(f"https://api.nasa.gov{endpoint}", params=params)
    response.raise_for_status()
    epic_images_data = response.json()

    available_image_urls = []
    for image_item in epic_images_data[:count]:
        date_time_str = image_item['date']
        date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        formatted_date = date_time.strftime("%Y/%m/%d")
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{formatted_date}/png/{image_item['image']}.png"
        if is_image_available(image_url):
            available_image_urls.append(image_url)

    return available_image_urls

def download_epic_images(count=5):
    """Скачивает EPIC изображения и сохраняет их в каталог."""
    api_key = os.getenv('NASA_API_KEY')
    epic_image_urls = fetch_epic_image_urls(api_key, count)
    for index, image_url in enumerate(epic_image_urls, start=1):
        save_image(image_url, EPIC_IMAGES_DIRECTORY, f"epic_image_{index}.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Скачать изображения из EPIC.')
    parser.add_argument('--count', type=int, default=5, help='Количество изображений для скачивания.')
    args = parser.parse_args()
    download_epic_images(args.count)