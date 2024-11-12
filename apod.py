import requests
from dotenv import load_dotenv
from download_tools import save_image

def get_apod_images(api_key, count=1):
    """Получает изображения APOD из NASA API."""
    params = {
        'api_key': api_key,
        'count': count
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    response.raise_for_status()
    return response.json()

def extract_image_urls(apod_images):
    """Извлекает URL изображений из полученных данных APOD."""
    return [image['url'] for image in apod_images if 'url' in image]

def download_apod_images(count=1, api_key=None):
    """Скачивает изображения APOD и возвращает их содержимое в виде списка байтов."""
    apod_images = get_apod_images(api_key, count)
    if apod_images:
        image_urls = extract_image_urls(apod_images)
        return [save_image(url) for url in image_urls]
    return []

def get_apod_images(api_key, count=1):
    """Получает изображения APOD из NASA API."""


if __name__ == "__main__":
    api_key_nasa = os.getenv('NASA_API_KEY')
    images = get_apod_images(api_key_nasa, count=1)
    print(images)
























