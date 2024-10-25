#main
import subprocess
import os
import time
from dotenv import load_dotenv


def load_config():
    """Загружает конфигурацию из переменных окружения."""
    load_dotenv()
    return {
        "DOWNLOAD_INTERVAL": int(os.getenv('DOWNLOAD_INTERVAL', 14400)),  # По умолчанию 4 часа
    }


def run_download_script():
    """Запускает скрипт для скачивания изображений."""
    subprocess.Popen(['python', 'download_apod.py'])
    subprocess.Popen(['python', 'download_epic.py'])
    subprocess.Popen(['python', 'download_spacex.py'])


def run_publish_script():
    """Запускает скрипт для публикации изображений."""
    subprocess.Popen(['python', 'publish_images.py'])


def main():
    run_download_script()
    run_publish_script()

    # Ожидаем, пока процессы будут выполняться
    config = load_config()
    print(f"Скрипт работает. Ожидание следующего обновления через {config['DOWNLOAD_INTERVAL']} секунд...")

    while True:
        time.sleep(config['DOWNLOAD_INTERVAL'])  # Подождать указанный интервал


if __name__ == "__main__":
    main()