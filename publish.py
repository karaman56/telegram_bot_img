import os
import argparse
from dotenv import load_dotenv
from apod import download_apod_images
from epic import download_epic_images
from spacex import download_spacex_image

IMAGES_DIRECTORY = "./images"

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Загрузка изображений.')
    parser.add_argument('--count', type=int, default=1,
                        help='Количество изображений для загрузки из каждого источника (по умолчанию 1).')
    args = parser.parse_args()
    nasa_api_key = os.getenv('NASA_API_KEY')
    download_apod_images(count=args.count, api_key=nasa_api_key)
    download_epic_images(count=args.count, api_key=nasa_api_key)
    download_spacex_image()  # Предполагается, что эта функция загружает одно изображение

if __name__ == "__main__":
    main()














