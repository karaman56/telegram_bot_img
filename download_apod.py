# download_apod.py
import requests
from general_functions import is_image_available, save_image

def fetch_apod_image_urls(api_key, image_count=5):
    """Получает URL изображений из Astronomy Picture of the Day."""
    endpoint = "/planetary/apod"
    params = {"api_key": api_key, "count": image_count}

    response = requests.get(f"https://api.nasa.gov{endpoint}", params=params)
    response.raise_for_status()

    apod_image_response = response.json()
    return [image_item['url'] for image_item in apod_image_response if image_item['media_type'] == 'image']

def download_apod_images(image_urls, download_directory):
    """Скачивает APOD изображения и сохраняет их в указанный каталог."""
    for index, image_url in enumerate(image_urls, start=1):
        if is_image_available(image_url):
            image_filename = f"apod_image_{index}.jpg"
            save_image(image_url, download_directory, image_filename)