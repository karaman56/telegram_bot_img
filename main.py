
import os
import time
import argparse
from dotenv import load_dotenv
from publish import publish_images_to_telegram

def load_images():
    """Загружает изображения из локальной директории."""
    image_files = []
    for filename in os.listdir('./apod_images'):
        with open(os.path.join('./apod_images', filename), 'rb') as f:
            image_files.append(f.read())
    for filename in os.listdir('./epic_images'):
        with open(os.path.join('./epic_images', filename), 'rb') as f:
            image_files.append(f.read())
    if os.path.exists('./spacex_images/patch.png'):
        with open('./spacex_images/patch.png', 'rb') as f:
            image_files.append(f.read())
    return image_files

def main():
    load_dotenv()
    bot_token_key = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id_key = os.getenv('TELEGRAM_CHANNEL_ID')

    parser = argparse.ArgumentParser(description='Публикация изображений в Telegram.')
    args = parser.parse_args()

    while True:
        image_bytes = load_images()
        for image in image_bytes:
            publish_images_to_telegram(image, bot_token_key, chat_id_key)
            print("Изображение опубликовано. Ждем 4 часа перед следующей публикацией...")
            time.sleep(14400)

if __name__ == "__main__":
    main()




