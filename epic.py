import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
from download_tools import save_image



def get_epic_images(api_key):
    """Получает информацию о изображениях EPIC из NASA API."""
    params = {'api_key': api_key}
    query_string = urlencode(params)
    url = f'https://api.nasa.gov/EPIC/api/natural/all?{query_string}'

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
    pass

def main():
    api_key_epic = os.getenv('EPIC_API_KEY')
    images = download_epic_images(count=1, api_key=api_key_epic)
    print(images)

if __name__ == "__main__":
    main()























