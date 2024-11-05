import os
import requests
from dotenv import load_dotenv
from download_tools import save_image

APOD_IMAGES_DIRECTORY = "./apod_images"

def get_apod_images(api_key, count=1):
    """Получает изображения APOD из NASA API."""
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&count={count}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def download_apod_images(count=1, api_key=None):
    """Скачивает изображения APOD и возвращает их содержимое в виде списка байтов."""
    apod_images = get_apod_images(api_key, count)
    images = []
    for image in apod_images:
        if 'url' in image:
            images.append(save_image(image['url']))
    return images

if __name__ == "__main__":
    load_dotenv()
    api_key_nasa = os.getenv('NASA_API_KEY')
    download_apod_images(count=1, api_key=api_key_nasa)





















