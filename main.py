import os
import time
from dotenv import load_dotenv
from telegram import Bot
from nasa_api import fetch_apod_images, fetch_epic_images
from spacex_api import fetch_spacex_image
from image_utils import download_image
from telegram_publisher import publish_images

load_dotenv()

NASA_API_KEY = os.getenv('NASA_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
PUBLISH_INTERVAL = int(os.getenv('PUBLISH_INTERVAL', 14400))
APOD_IMAGES_DIRECTORY = os.getenv('APOD_IMAGES_DIRECTORY', './apod_images')
EPIC_IMAGES_DIRECTORY = os.getenv('EPIC_IMAGES_DIRECTORY', './epic_images')
SPACEX_IMAGES_DIRECTORY = './spacex_images'

if any(v is None for v in [NASA_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID]):
    raise ValueError("Отсутствует один или несколько обязательных параметров в переменных окружения.")

def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    while True:
        # Получение и загрузка изображений APOD
        apod_image_urls = fetch_apod_images(count=5)
        for index, image_url in enumerate(apod_image_urls, start=1):
            download_image(image_url, APOD_IMAGES_DIRECTORY, f"apod_image_{index}.jpg")

        # Получение и загрузка изображений EPIC
        epic_image_urls = fetch_epic_images(count=5)
        for index, image_url in enumerate(epic_image_urls, start=1):
            download_image(image_url, EPIC_IMAGES_DIRECTORY, f"epic_image_{index}.png")

        # Получение и загрузка изображения SpaceX
        spacex_image_url = fetch_spacex_image()
        if spacex_image_url:
            download_image(spacex_image_url, SPACEX_IMAGES_DIRECTORY, "spacex_image.jpg")

        # Публикация всех изображений
        publish_images(bot, APOD_IMAGES_DIRECTORY)
        publish_images(bot, EPIC_IMAGES_DIRECTORY)
        publish_images(bot, SPACEX_IMAGES_DIRECTORY)

        print(f"Ожидание следующего обновления через {PUBLISH_INTERVAL} секунд...")
        time.sleep(PUBLISH_INTERVAL)

if __name__ == "__main__":
    main()