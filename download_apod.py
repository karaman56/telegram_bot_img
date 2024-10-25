# download_apod.py
import requests
from urllib.parse import urlencode
from general_functions import save_image

def fetch_apod_image_urls(api_key, image_count=1):
    """Получает URL изображений из Astronomy Picture of the Day (APOD)."""
    endpoint = "/planetary/apod"
    params = {"api_key": api_key, "count": image_count}
    query_string = urlencode(params)
    response = requests.get(f"https://api.nasa.gov{endpoint}?{query_string}")
    response.raise_for_status()
    apod_image_data = response.json()
    return [image_item['url'] for image_item in apod_image_data if image_item['media_type'] == 'image']

def download_apod_images(api_key, download_directory, image_count=1):
    """Скачивает изображения APOD и сохраняет их в указанный каталог."""
    image_urls = fetch_apod_image_urls(api_key, image_count)
    for index, image_url in enumerate(image_urls, start=1):
        image_filename = f"apod_image_{index}.jpg"
        save_image(image_url, download_directory, image_filename)