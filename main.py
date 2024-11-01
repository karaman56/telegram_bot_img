import os
import time
import argparse
from dotenv import load_dotenv
from apod import download_apod_images
from epic import download_epic_images
from spacex import download_spacex_image
from publish import publish_images_to_telegram

def download_images(api_key, count):
    download_apod_images(count=count, api_key=api_key)
    download_epic_images(count=count, api_key=api_key)
    download_spacex_image()

def main():
    load_dotenv()
    API_KEY = os.getenv('NASA_API_KEY')
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    CHAT_ID = os.getenv('TELEGRAM_CHANNEL_ID')

    parser = argparse.ArgumentParser(description='Загрузка и публикация изображений в Telegram.')
    parser.add_argument('--count', type=int, default=3, help='Количество изображений для загрузки (по умолчанию 3).')
    args = parser.parse_args()

    while True:
        print("Начинаем загрузку изображений...")
        download_images(API_KEY, args.count)
        print("Загрузка завершена. Публикуем изображения в Telegram...")
        publish_images_to_telegram('./apod_images', BOT_TOKEN, CHAT_ID)
        publish_images_to_telegram('./epic_images', BOT_TOKEN, CHAT_ID)
        publish_images_to_telegram('./spacex_images', BOT_TOKEN, CHAT_ID)
        print("Публикация завершена. Ждем 4 часа перед следующей загрузкой и публикацией...")
        time.sleep(14400)  # 4 часа в секундах

if __name__ == "__main__":
    main()



