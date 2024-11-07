
import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
from download_tools import save_image

SPACEX_IMAGES_DIRECTORY = "./spacex_images"

def get_the_latest_launch_photo(params=None):
    """Получает информацию о последнем запуске SpaceX."""
    base_url = 'https://api.spacexdata.com/v4/launches/latest'
    if params:
        query_string = urlencode(params)  # Кодируем параметры
        url = f"{base_url}?{query_string}"  # Формируем URL с параметрами
    else:
        url = base_url

    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def extract_image_url(launch_data):
    """Извлекает URL изображения из данных о запуске."""
    return launch_data["links"]["patch"]["large"]

def download_spacex_image():
    """Скачивает изображение последнего запуска SpaceX и возвращает его содержимое в виде байтов."""
    the_latest_launch_photo = get_the_latest_launch_photo()
    if not the_latest_launch_photo:
        return None
    image_url = extract_image_url(the_latest_launch_photo)
    if not image_url:
        return None
    return save_image(image_url)

if __name__ == "__main__":
    load_dotenv()
    image_bytes = download_spacex_image()
    if image_bytes:
        print("Скачано изображение SpaceX.")


















