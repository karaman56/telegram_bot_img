import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
from download_tools import save_image  # Импортируем функцию save_image

EPIC_IMAGES_DIRECTORY = "./epic_images"

def get_epic_images(api_key):
    """Получает информацию о изображениях EPIC из NASA API."""
    params = {'api_key': api_key}
    url = 'https://api.nasa.gov/EPIC/api/natural/all?' + urlencode(params)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def download_epic_images(count=1, api_key=None):
    """Скачивает изображения EPIC и сохраняет их в указанной директории."""
    os.makedirs(EPIC_IMAGES_DIRECTORY, exist_ok=True)
    epic_images = get_epic_images(api_key)[:count]
    for item in epic_images:
        date_str = item['date'].split(' ')[0].replace('-', '/')
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date_str}/png/{item['image']}.png"
        print(f"EPIC Image URL: {image_url}")
        file_path = save_image(image_url, EPIC_IMAGES_DIRECTORY, f"epic_{date_str}")
        if file_path:
            print(f"Скачано изображение EPIC: {file_path}")

if __name__ == "__main__":
    load_dotenv()
    api_key_nasa = os.getenv('NASA_API_KEY')
    download_epic_images(count=3, api_key=api_key_nasa)












