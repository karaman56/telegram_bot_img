import os
import time
import argparse
import random
from dotenv import load_dotenv
from telegram import Bot

def load_environment():
    load_dotenv()

def publish_images(directory):
    load_environment()

    token = os.getenv('TELEGRAM_BOT_TOKEN')
    channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
    publish_interval = int(os.getenv('PUBLISH_INTERVAL', 14400))  # 4 часа по умолчанию

    if token is None or channel_id is None:
        print("Ошибка: переменные окружения TELEGRAM_BOT_TOKEN или TELEGRAM_CHANNEL_ID не установлены.")
        return

    bot = Bot(token=token)

    if not os.path.exists(directory) or not os.listdir(directory):
        print(f"Ошибка: директория '{directory}' пуста или не существует.")
        return

    images = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png'))]

    while True:
        random.shuffle(images)
        selected_images = images[:5]  # Выбираем 5 случайных изображений

        for image in selected_images:
            image_path = os.path.join(directory, image)
            print(f"Отправка изображения: {image_path}")
            with open(image_path, 'rb') as photo:
                bot.send_photo(chat_id=channel_id, photo=photo)
            time.sleep(5)  # Задержка между отправками

        time.sleep(publish_interval)  # Задержка перед следующим циклом

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Publish images to Telegram channel.')
    parser.add_argument('--directory', required=True, help='Directory containing images to publish.')
    args = parser.parse_args()
    publish_images(args.directory)
