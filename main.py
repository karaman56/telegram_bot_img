#main
import os
import time
from dotenv import load_dotenv
from telegram import Bot
from telegram_publisher import publish_images_from_directory
from download_apod import download_apod_images
from download_epic import download_earth_images
from download_spacex import download_spacex_image

def load_config():
    """Загружает конфигурацию из переменных окружения."""
    load_dotenv()
    return {
        "TELEGRAM_BOT_TOKEN": os.getenv('TELEGRAM_BOT_TOKEN'),
        "NASA_API_KEY": os.getenv('NASA_API_KEY'),
        "APOD_IMAGES_DIRECTORY": os.getenv('APOD_IMAGES_DIRECTORY', './apod_images'),
        "EPIC_IMAGES_DIRECTORY": os.getenv('EPIC_IMAGES_DIRECTORY', './epic_images'),
        "SPACEX_IMAGES_DIRECTORY": './spacex_images',
        "PUBLISH_INTERVAL": int(os.getenv('PUBLISH_INTERVAL', 14400))  # По умолчанию 4 часа
    }

def main():
    config = load_config()
    telegram_bot = Bot(token=config['TELEGRAM_BOT_TOKEN'])

    while True:
        # Скачивание изображений APOD
        print("Скачивание изображений APOD...")
        download_apod_images(config['NASA_API_KEY'], config['APOD_IMAGES_DIRECTORY'], image_count=1)
        publish_images_from_directory(telegram_bot, config['APOD_IMAGES_DIRECTORY'])

        # Скачивание изображений EPIC
        print("\nСкачивание изображений EPIC...")
        download_earth_images(config['NASA_API_KEY'], config['EPIC_IMAGES_DIRECTORY'], max_image_count=1)
        publish_images_from_directory(telegram_bot, config['EPIC_IMAGES_DIRECTORY'])

        # Скачивание и публикация изображения SpaceX
        print("\nСкачивание изображения SpaceX...")
        download_spacex_image(download_directory=config['SPACEX_IMAGES_DIRECTORY'])
        publish_images_from_directory(telegram_bot, config['SPACEX_IMAGES_DIRECTORY'])

        print(f"\nОжидание следующего обновления через {config['PUBLISH_INTERVAL']} секунд...")
        time.sleep(config['PUBLISH_INTERVAL'])

if __name__ == "__main__":
    main()