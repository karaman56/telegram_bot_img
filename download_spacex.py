# download_spacex.py
import requests
import os
from dotenv import load_dotenv
from general_functions import save_image
import argparse

load_dotenv()
SPACEX_IMAGES_DIRECTORY = './spacex_images'


def fetch_spacex_image_url(launch_id=None):
    """Получает URL изображения для указанного запуска SpaceX."""
    base_url = 'https://api.spacexdata.com/v5/launches'
    params = {}

    if launch_id:
        url = f"{base_url}/{launch_id}"
    else:
        url = f"{base_url}/latest"

    response = requests.get(url)
    response.raise_for_status()
    launch_data = response.json()
    image_url = launch_data['links']['patch']['large']
    return image_url


def download_spacex_image(launch_id=None):
    """Скачивает изображение SpaceX и сохраняет его в каталог."""
    spacex_image_url = fetch_spacex_image_url(launch_id)
    if spacex_image_url:
        save_image(spacex_image_url, SPACEX_IMAGES_DIRECTORY, "spacex_image.jpg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Скачать изображение SpaceX.')
    parser.add_argument('--launch_id', type=str,
                        help='ID запуска SpaceX. Если не указано, будет загружено последнее изображение.')
    args = parser.parse_args()
    download_spacex_image(args.launch_id)
