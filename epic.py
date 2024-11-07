
import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
from download_tools import save_image

EPIC_IMAGES_DIRECTORY = "./epic_images"

def get_epic_images(api_key):
    """Получает информацию о изображениях EPIC из NASA API."""
    params = {'api_key': api_key}
    query_string = urlencode(params)
    url = f'https://api.nasa.gov/EPIC/api/natural/all?{query_string}'

    # Проверка на наличие символа '?'
    if '?' in url:
        raise ValueError("URL содержит символ '?', что недопустимо.")

    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def format_date(date_str):
    """Форматирует строку даты для использования в URL."""
    return date_str.split(' ')[0].replace('-', '/')

def construct_image_url(image):
    """Создает URL изображения на основе данных EPIC."""
    date_str = format_date(image['date'])
    return f"https://epic.gsfc.nasa.gov/archive/natural/{date_str}/png/{image['image']}.png"

def download_images(image_urls):
    """Скачивает изображения по списку URL и возвращает их содержимое в виде списка байтов."""
    images = []
    for url in image_urls:
        images.append(save_image(url))
    return images

def download_epic_images(count=1, api_key=None):
    """Скачивает изображения EPIC и возвращает их содержимое в виде списка байтов."""
    epic_images = get_epic_images(api_key)[:count]  # Получаем только нужное количество изображений
    image_urls = [construct_image_url(image) for image in epic_images]  # Формируем URL для изображений
    return download_images(image_urls)

if __name__ == "__main__":
    load_dotenv()
    api_key_nasa = os.getenv('NASA_API_KEY')
    download_epic_images(count=1, api_key=api_key_nasa)  
























