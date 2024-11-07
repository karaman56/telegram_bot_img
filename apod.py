
import os
import requests
from dotenv import load_dotenv
from download_tools import save_image
from urllib.parse import urlencode

APOD_IMAGES_DIRECTORY = "./apod_images"

def get_apod_images(api_key, count=1):
    """Получает изображения APOD из NASA API."""
    params = {
        'api_key': api_key,
        'count': count
    }
    query_string = urlencode(params)
    url = f'https://api.nasa.gov/planetary/apod?{query_string}'
    if '?' in url:
        raise ValueError("URL содержит символ '?', что недопустимо.")
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def extract_image_urls(apod_images):
    """Извлекает URL изображений из полученных данных APOD."""
    return [image['url'] for image in apod_images if 'url' in image]

def download_images(image_urls):
    """Скачивает изображения по списку URL и возвращает их содержимое в виде списка байтов."""
    images = []
    for url in image_urls:
        images.append(save_image(url))
    return images

def download_apod_images(count=1, api_key=None):
    """Скачивает изображения APOD и возвращает их содержимое в виде списка байтов."""
    apod_images = get_apod_images(api_key, count)
    image_urls = extract_image_urls(apod_images)
    return download_images(image_urls)

if __name__ == "__main__":
    load_dotenv()
    api_key_nasa = os.getenv('NASA_API_KEY')
    download_apod_images(count=1, api_key=api_key_nasa)


























