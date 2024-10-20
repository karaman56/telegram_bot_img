
import os
import time
from dotenv import load_dotenv
from telegram import Bot
from telegram_publisher import publish_images
from download_apod import download_apod_images
from download_epic import download_epic_images
from download_spacex import download_spacex_image

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
NASA_API_KEY = os.getenv('NASA_API_KEY')
PUBLISH_INTERVAL = int(os.getenv('PUBLISH_INTERVAL'))
APOD_IMAGES_DIRECTORY = os.getenv('APOD_IMAGES_DIRECTORY')
EPIC_IMAGES_DIRECTORY = os.getenv('EPIC_IMAGES_DIRECTORY')
SPACEX_IMAGES_DIRECTORY = './spacex_images'

def start_image_fetcher():
    """Запускает процесс получения изображений и их публикации в Telegram."""
    telegram_bot = Bot(token=TELEGRAM_BOT_TOKEN)

    while True:
        print("Скачивание изображений APOD...")
        download_apod_images()

        print("Скачивание изображений EPIC...")
        download_epic_images()

        print("Скачивание изображения SpaceX...")
        download_spacex_image()


        publish_images(telegram_bot, './apod_images')
        publish_images(telegram_bot, './epic_images')
        publish_images(telegram_bot, './spacex_images')

        print(f"Ожидание следующего обновления через {PUBLISH_INTERVAL} секунд...")
        time.sleep(PUBLISH_INTERVAL)

if __name__ == "__main__":
    start_image_fetcher()
