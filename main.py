
import os
import time
import random
from datetime import datetime
import requests
from dotenv import load_dotenv
from telegram import Bot
from urllib.parse import urlencode


# Загружаем переменные окружения
def load_environment():
    load_dotenv()


# Константы конфигурации
NASA_API_KEY =  os.getenv('NASA_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
PUBLISH_INTERVAL = int(os.getenv('PUBLISH_INTERVAL', 14400))  # 4 часа по умолчанию
APOD_IMAGES_DIRECTORY = os.getenv('APOD_IMAGES_DIRECTORY', './apod_images')
EPIC_IMAGES_DIRECTORY = os.getenv('EPIC_IMAGES_DIRECTORY', './epic_images')

# Проверяем наличие ключей
if any(v is None for v in [NASA_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID]):
    raise ValueError("Отсутствует один или несколько обязательных параметров в переменных окружения.")


# Функция для загрузки изображений с NASA APOD
def fetch_apod_images(count=5):
    endpoint = "/planetary/apod"
    params = {"api_key": NASA_API_KEY, "count": count}
    url = f"https://api.nasa.gov{endpoint}?{urlencode(params)}"

    response = requests.get(url)
    response.raise_for_status()

    apod_image_data = response.json()
    image_urls = [item['url'] for item in apod_image_data if item['media_type'] == 'image']

    return image_urls


# Функция для загрузки изображений с NASA EPIC
def fetch_epic_images(count=5):
    endpoint = "/EPIC/api/natural/images"
    params = {"api_key": NASA_API_KEY}
    url = f"https://api.nasa.gov{endpoint}?{urlencode(params)}"

    response = requests.get(url)
    response.raise_for_status()

    epic_image_data = response.json()

    image_urls = []
    for item in epic_image_data[:count]:
        date_time_str = item['date']
        date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        date_str = date_time.strftime("%Y/%m/%d")
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date_str}/png/{item['image']}.png"
        image_urls.append(image_url)

    return image_urls


# Функция для скачивания изображений
def download_image(image_url, save_directory, filename):
    response = requests.get(image_url)
    response.raise_for_status()

    file_path = os.path.join(save_directory, filename)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Изображение загружено: {file_path}")


# Функция для публикации изображений в Telegram
def publish_images(bot, directory):
    if not os.path.exists(directory) or not os.listdir(directory):
        print(f"Ошибка: директория '{directory}' пуста или не существует.")
        return

    images = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png'))]

    random.shuffle(images)
    selected_images = images[:5]

    for image in selected_images:
        image_path = os.path.join(directory, image)
        print(f"Отправка изображения: {image_path}")
        with open(image_path, 'rb') as photo:
            bot.send_photo(chat_id=TELEGRAM_CHANNEL_ID, photo=photo)
        time.sleep(5)


# Основная функция
def main():
    load_environment()

    # Создаем директории, если они не существуют
    os.makedirs(APOD_IMAGES_DIRECTORY, exist_ok=True)
    os.makedirs(EPIC_IMAGES_DIRECTORY, exist_ok=True)

    # Создаем бота для Telegram
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    while True:
        # Загружаем изображения
        apod_image_urls = fetch_apod_images(count=5)
        for index, image_url in enumerate(apod_image_urls, start=1):
            download_image(image_url, APOD_IMAGES_DIRECTORY, f"apod_image_{index}.jpg")

        epic_image_urls = fetch_epic_images(count=5)
        for index, image_url in enumerate(epic_image_urls, start=1):
            download_image(image_url, EPIC_IMAGES_DIRECTORY, f"epic_image_{index}.png")

        # Публикуем изображения в Telegram
        publish_images(bot, APOD_IMAGES_DIRECTORY)
        publish_images(bot, EPIC_IMAGES_DIRECTORY)

        # Ждем перед следующим циклом
        print(f"Ожидание следующего обновления через {PUBLISH_INTERVAL} секунд...")
        time.sleep(PUBLISH_INTERVAL)


if __name__ == "__main__":
    main()
