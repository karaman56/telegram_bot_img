import os
import time
import random
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
    bot_token_key = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id_key = os.getenv('TELEGRAM_CHANNEL_ID')
    nasa_api_key = os.getenv('NASA_API_KEY')

    while True:
        download_apod_images(count=1, api_key=nasa_api_key)
        download_epic_images(count=1, api_key=nasa_api_key)
        download_spacex_image()

        image_bytes = load_images()

        random.shuffle(image_bytes)
        for image in image_bytes:
            publish_images_to_telegram(image, bot_token_key, chat_id_key)
            print("Изображение опубликовано. Ждем 4 часа перед следующей публикацией...")
            time.sleep(14400)


if __name__ == "__main__":
    main()


