import os
import requests
from dotenv import load_dotenv
from download_tools import save_image


def get_epic_images(api_key):
    """Получает информацию о изображениях EPIC из NASA API."""
    url = 'https://api.nasa.gov/EPIC/api/natural/all'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
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


def main():
    load_dotenv()
    api_key_epic = os.getenv('EPIC_API_KEY')
    epic_images = get_epic_images(api_key_epic)
    count = 1
    image_urls = [construct_image_url(image) for image in epic_images[:count]]
    images = download_images(image_urls)

if __name__ == "__main__":
    main()

























