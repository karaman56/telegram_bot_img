import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
from download_tools import save_image

EPIC_IMAGES_DIRECTORY = "./epic_images"

def get_epic_images(api_key):
    """Получает информацию о изображениях EPIC из NASA API."""
    params = {'api_key': api_key}
    url = 'https://api.nasa.gov/EPIC/api/natural/all?' + urlencode(params)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def download_epic_images(count=1, api_key=None):
    """Скачивает изображения EPIC и возвращает их содержимое в виде списка байтов."""
    epic_images = get_epic_images(api_key)[:count]
    images = []
    for image in epic_images:
        date_str = image['date'].split(' ')[0].replace('-', '/')
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date_str}/png/{image['image']}.png"
        images.append(save_image(image_url))
    return images

if __name__ == "__main__":
    load_dotenv()
    api_key_nasa = os.getenv('NASA_API_KEY')
    download_epic_images(count=1, api_key=api_key_nasa)














