import os
import time
import random
import argparse
from dotenv import load_dotenv
from publish import publish_images_to_telegram
from apod import download_apod_images
from epic import download_epic_images
from spacex import download_spacex_image

IMAGES_DIRECTORY = "./images"


def load_images():
    """Загружает изображения из локальной директории."""
    image_files = []
    if not os.path.exists(IMAGES_DIRECTORY):
        os.makedirs(IMAGES_DIRECTORY)

    for filename in os.listdir(IMAGES_DIRECTORY):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            with open(os.path.join(IMAGES_DIRECTORY, filename), 'rb') as f:
                image_files.append(f.read())
    return image_files


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Загрузка и публикация изображений в Telegram.')
    parser.add_argument('--count', type=int, default=1,
                        help='Количество изображений для загрузки из каждого источника (по умолчанию 1).')
    parser.add_argument('--publish_interval', type=int, default=14400,
                        help='Интервал публикации изображений в секундах (по умолчанию 14400, это 4 часа).')
    args = parser.parse_args()

    bot_token_key = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id_key = os.getenv('TELEGRAM_CHANNEL_ID')
    nasa_api_key = os.getenv('NASA_API_KEY')

    while True:

        download_apod_images(count=args.count, api_key=nasa_api_key)
        download_epic_images(count=args.count, api_key=nasa_api_key)
        download_spacex_image()
        image_bytes = load_images()
        random.shuffle(image_bytes)  # Перемешиваем изображения
        for image in image_bytes:
            publish_images_to_telegram(image, bot_token_key, chat_id_key)
            print(
                "Изображение опубликовано. Ждем {} секунд перед следующей публикацией...".format(args.publish_interval))
            time.sleep(args.publish_interval)  


if __name__ == "__main__":
    main()

