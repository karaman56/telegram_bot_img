import os
import time
import argparse
from dotenv import load_dotenv
from apod import download_apod_images
from epic import download_epic_images
from spacex import download_spacex_image

def download_images(api_key, count):
    """Загружает изображения из APOD, EPIC и SpaceX."""
    apod_images = download_apod_images(count=count, api_key=api_key)
    epic_images = download_epic_images(count=count, api_key=api_key)
    spacex_image = download_spacex_image()
    return apod_images, epic_images, spacex_image

def main():
    load_dotenv()
    api_key_nasa = os.getenv('NASA_API_KEY')

    parser = argparse.ArgumentParser(description='Загрузка изображений.')
    parser.add_argument('--count', type=int, default=3, help='Количество изображений для загрузки (по умолчанию 3).')
    args = parser.parse_args()

    while True:
        download_images(api_key_nasa, args.count)
        print("Загрузка завершена. Ждем 4 часа перед следующей загрузкой...")
        time.sleep(14400)

if __name__ == "__main__":
    main()

