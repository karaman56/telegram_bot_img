import os
import time
import random
import argparse
from dotenv import load_dotenv
from publish import publish_images_to_telegram
from load_images import load_images
from apod import download_apod_images
from epic import download_epic_images
from spacex import download_spacex_image

IMAGES_DIRECTORY = "./images"

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Загрузка и публикация изображений в Telegram.')
    parser.add_argument('--count', type=int, default=1,
                        help='Количество изображений для загрузки из каждого источника (по умолчанию 1).')
    args = parser.parse_args()

    nasa_api_key = os.getenv('NASA_API_KEY')
    bot_token_key = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id_key = os.getenv('TELEGRAM_CHANNEL_ID')

    # Загрузка изображений
    download_apod_images(count=args.count, api_key=nasa_api_key)
    download_epic_images(count=args.count, api_key=nasa_api_key)
    download_spacex_image()

    while True:
        image_bytes = load_images()
        random.shuffle(image_bytes)

        for image in image_bytes:
            publish_images_to_telegram(image, bot_token_key, chat_id_key)
            print("Изображение опубликовано. Ждем 4 часа перед следующей публикацией...")
            time.sleep(14400)
            """break прерыват цикл и публикует только одну фотографию и публикует через 4 час следующую, без этого будут публиковаться 5"""
            break

if __name__ == "__main__":
    main()



