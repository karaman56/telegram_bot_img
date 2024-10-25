import os
from dotenv import load_dotenv
from telegram import Bot
from telegram_publisher import publish_images_from_directory


def load_config():
    """Загружает конфигурацию из переменных окружения."""
    load_dotenv()
    return {
        "TELEGRAM_BOT_TOKEN": os.getenv('TELEGRAM_BOT_TOKEN'),
        "APOD_IMAGES_DIRECTORY": os.getenv('APOD_IMAGES_DIRECTORY', './apod_images'),
        "EPIC_IMAGES_DIRECTORY": os.getenv('EPIC_IMAGES_DIRECTORY', './epic_images'),
        "SPACEX_IMAGES_DIRECTORY": './spacex_images',
    }


def publish_images():
    config = load_config()
    telegram_bot = Bot(token=config['TELEGRAM_BOT_TOKEN'])

    print("Начинаю публикацию изображений...")

    # Публикация изображений
    try:
        print("Публикация изображений APOD...")
        publish_images_from_directory(telegram_bot, config['APOD_IMAGES_DIRECTORY'])

        print("\nПубликация изображений EPIC...")
        publish_images_from_directory(telegram_bot, config['EPIC_IMAGES_DIRECTORY'])

        print("\nПубликация изображений SpaceX...")
        publish_images_from_directory(telegram_bot, config['SPACEX_IMAGES_DIRECTORY'])
    except Exception as e:
        print(f"Ошибка при публикации изображений: {e}")


if __name__ == "__main__":
    publish_images()