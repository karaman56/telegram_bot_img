import os
from dotenv import load_dotenv

def check_env():
    # Загружаем переменные окружения из .env файла
    load_dotenv()

    required_variables = [
        'TELEGRAM_BOT_TOKEN',
        'TELEGRAM_CHANNEL_ID',
        'NASA_API_KEY',
        'PUBLISH_INTERVAL',
        'APOD_IMAGES_DIRECTORY',
        'EPIC_IMAGES_DIRECTORY'
    ]

    missing_variables = [var for var in required_variables if os.getenv(var) is None]

    if missing_variables:
        print("Отсутствуют следующие переменные окружения:")
        for var in missing_variables:
            print(f"- {var}")
    else:
        print("Все необходимые переменные окружения установлены.")

if __name__ == "__main__":
    check_env()