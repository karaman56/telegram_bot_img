#main
import os
import time
from dotenv import load_dotenv
from telegram import Bot
from telegram_publisher import publish_images
from download_apod import fetch_apod_image_urls, download_apod_images
from download_epic import fetch_epic_image_urls, download_epic_images
from download_spacex import download_spacex_image


def main():
    load_dotenv()

    config = {
        "telegram_bot_token": os.getenv('TELEGRAM_BOT_TOKEN'),
        "telegram_channel_id": os.getenv('TELEGRAM_CHANNEL_ID'),
        "nasa_api_key": os.getenv('NASA_API_KEY'),
        "publish_interval": int(os.getenv('PUBLISH_INTERVAL', 3600)),
        "apod_images_directory": os.getenv('APOD_IMAGES_DIRECTORY', './apod_images'),
        "epic_images_directory": os.getenv('EPIC_IMAGES_DIRECTORY', './epic_images'),
        "spaces_images_directory": './spacex_images'
    }

    start_image_fetcher(config)


def start_image_fetcher(config):
    """Запускает процесс получения изображений и их публикации в Telegram."""
    telegram_bot = Bot(token=config['telegram_bot_token'])

    while True:

        process_apod_images(telegram_bot, config)
        process_epic_images(telegram_bot, config)
        process_spacex_images(telegram_bot, config)

        print(f"Ожидание следующего обновления через {config['publish_interval']} секунд...")
        time.sleep(config['publish_interval'])


def process_apod_images(telegram_bot, config):
    """Скачивание и публикация APOD изображений."""
    print("Скачивание изображений APOD...")
    apod_image_urls = fetch_apod_image_urls(config['nasa_api_key'])
    download_apod_images(apod_image_urls, config['apod_images_directory'])
    publish_images(telegram_bot, config['apod_images_directory'])


def process_epic_images(telegram_bot, config):
    """Скачивание и публикация EPIC изображений."""
    print("Скачивание изображений EPIC...")
    epic_image_urls = fetch_epic_image_urls(config['nasa_api_key'])
    download_epic_images(epic_image_urls, config['epic_images_directory'])
    publish_images(telegram_bot, config['epic_images_directory'])


def process_spacex_images(telegram_bot, config):
    """Скачивание и публикация изображений SpaceX."""
    print("Скачивание изображения SpaceX...")
    download_spacex_image()
    publish_images(telegram_bot, config['spaces_images_directory'])


if __name__ == "__main__":
    main()