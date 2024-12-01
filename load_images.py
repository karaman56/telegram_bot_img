import os
import argparse
from dotenv import load_dotenv
from apod import download_apod_images
from epic import download_epic_images
from spacex import download_spacex_image

IMAGES_DIRECTORY = "./images"


def load_images():
    """Загружает изображения из локальной директории."""
    image_files = []

    # Создаем каталог, если его еще нет
    os.makedirs(IMAGES_DIRECTORY, exist_ok=True)

    for filename in os.listdir(IMAGES_DIRECTORY):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            with open(os.path.join(IMAGES_DIRECTORY, filename), 'rb') as f:
                image_files.append(f.read())
    return image_files


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Загрузка изображений.')
    parser.add_argument('--count', type=int, default=1,
                        help='Количество изображений для загрузки из каждого источника (по умолчанию 1).')
    args = parser.parse_args()

    nasa_api_key = os.getenv('NASA_API_KEY')

    download_apod_images(count=args.count, api_key=nasa_api_key)
    download_epic_images(count=args.count, api_key=nasa_api_key)
    download_spacex_image()


if __name__ == "__main__":
    main()




