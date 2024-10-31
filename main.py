import os
import argparse
from dotenv import load_dotenv
import time
from apod import download_apod_images
from epic import download_epic_images
from spacex import download_spacex_image
from telegram import publish_images_to_telegram

if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description='Скачивание и публикация изображений из NASA и SpaceX.')
    parser.add_argument('--count', type=int, default=3, help='Количество изображений для загрузки (по умолчанию 3).')
    parser.add_argument('--interval', type=int, default=14400, help='Интервал публикации в секундах (по умолчанию 14400).')

    args = parser.parse_args()

    API_KEY = os.getenv('NASA_API_KEY')
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

    while True:
        try:
            download_apod_images(count=args.count, api_key=API_KEY)
            download_epic_images(count=args.count, api_key=API_KEY)
            download_spacex_image()

            publish_images_to_telegram(APOD_IMAGES_DIRECTORY, BOT_TOKEN, CHAT_ID)
            publish_images_to_telegram(EPIC_IMAGES_DIRECTORY, BOT_TOKEN, CHAT_ID)
            publish_images_to_telegram(SPACEX_IMAGES_DIRECTORY, BOT_TOKEN, CHAT_ID)

            print('Изображения успешно опубликованы. Ждем перед следующей итерацией.')
        except Exception as error:
            print(f"Ошибка в основном цикле: {error}")

        time.sleep(args.interval)  # Ждем перед следующей итерацией
        print('Ждем перед следующей итерацией')

