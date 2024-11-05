import os
import time
import argparse
from dotenv import load_dotenv
from apod import download_apod_images
from epic import download_epic_images
from spacex import download_spacex_image
from publish import publish_images_to_telegram

def download_images(api_key, count):
    """Загружает изображения из APOD, EPIC и SpaceX."""
    apod_images = download_apod_images(count=count, api_key=api_key)
    epic_images = download_epic_images(count=count, api_key=api_key)
    spacex_image = download_spacex_image()
    return apod_images, epic_images, spacex_image

def main():
    load_dotenv()
    api_key_nasa = os.getenv('NASA_API_KEY')
    bot_token_key = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id_key = os.getenv('TELEGRAM_CHANNEL_ID')

    parser = argparse.ArgumentParser(description='Загрузка и публикация изображений в Telegram.')
    parser.add_argument('--count', type=int, default=3, help='Количество изображений для загрузки (по умолчанию 3).')
    args = parser.parse_args()

    while True:
        apod_images, epic_images, spacex_image = download_images(api_key_nasa, args.count)
        print("Загрузка завершена. Публикуем изображения в Telegram...")
        for image_bytes in apod_images:
            publish_images_to_telegram(image_bytes, bot_token_key, chat_id_key)
        for image_bytes in epic_images:
            publish_images_to_telegram(image_bytes, bot_token_key, chat_id_key)
        if spacex_image:
            publish_images_to_telegram(spacex_image, bot_token_key, chat_id_key)

        print("Публикация завершена. Ждем 4 часа перед следующей загрузкой и публикацией...")
        time.sleep(14400)

if __name__ == "__main__":
    main()




