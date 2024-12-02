
import os
import time
import random
import argparse
from dotenv import load_dotenv
from publish import publish_images_to_telegram
from load_images import load_images


def publish_images_to_telegram(image_bytes, bot_token_key, chat_id_key):
    """Отправляет изображение в Telegram канал или чат."""
    url = f'https://api.telegram.org/bot{bot_token_key}/sendPhoto'
    files = {'photo': image_bytes}
    data = {'chat_id': chat_id_key}
    response = requests.post(url, files=files, data=data)
    response.raise_for_status()

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Публикация изображений в Telegram.')
    parser.add_argument('--interval', type=int, default=14400,
                        help='Интервал между публикациями в секундах (по умолчанию 4 часа).')
    args = parser.parse_args()

    bot_token_key = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id_key = os.getenv('TELEGRAM_CHANNEL_ID')

    while True:
        image_bytes = load_images()
        random.shuffle(image_bytes)

        for image in image_bytes:
            publish_images_to_telegram(image, bot_token_key, chat_id_key)
            print("Изображение опубликовано. Ждем {} секунд перед следующей публикацией...".format(args.interval))
            time.sleep(args.interval)
            break

if __name__ == "__main__":
    main()












