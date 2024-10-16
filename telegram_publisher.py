# telegram_publisher.py
import os
import random
import time
from telegram import Bot


def publish_images(bot, directory):
    """Publishes images from a specified directory to a Telegram channel."""
    if not os.path.exists(directory) or not os.listdir(directory):
        print(f"Ошибка: директория '{directory}' пуста или не существует.")
        return

    images = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png'))]
    if not images:
        print(f"Нет доступных изображений для отправки в '{directory}'.")
        return

    random.shuffle(images)
    selected_images = images[:5]

    for image in selected_images:
        image_path = os.path.join(directory, image)
        print(f"Отправка изображения: {image_path}")

        with open(image_path, 'rb') as photo:
            bot.send_photo(chat_id=os.getenv('TELEGRAM_CHANNEL_ID'), photo=photo)

        time.sleep(5)