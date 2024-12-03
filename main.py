import os
import time
import random
import argparse
import requests
from dotenv import load_dotenv

IMAGES_DIRECTORY = "./images"

def publish_images_to_telegram(image_path, bot_token_key, chat_id_key):
    """Отправляет изображение в Telegram канал или чат."""
    with open(image_path, 'rb') as f:
        files = {'photo': f}
        response = requests.post(f'https://api.telegram.org/bot{bot_token_key}/sendPhoto', files=files, data={'chat_id': chat_id_key})
        response.raise_for_status()

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Публикация изображений в Telegram.')
    parser.add_argument('--interval', type=int, default=14400,
                        help='Интервал между публикациями в секундах (по умолчанию 4 часа).')
    args = parser.parse_args()

    bot_token_key = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id_key = os.getenv('TELEGRAM_CHANNEL_ID')

    # Получаем список всех изображений в директории
    images = [os.path.join(IMAGES_DIRECTORY, img) for img in os.listdir(IMAGES_DIRECTORY) if img.endswith(('.png', '.jpg', '.jpeg'))]

    while True:
        if not images:
            print("Нет доступных изображений для публикации.")
            break

        # Случайный выбор изображения
        image_path = random.choice(images)
        publish_images_to_telegram(image_path, bot_token_key, chat_id_key)
        print(f"Изображение {image_path} опубликовано. Ждем {args.interval} секунд перед следующей публикацией...")
        time.sleep(args.interval)

if __name__ == "__main__":
    main()







