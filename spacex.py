import requests
from urllib.parse import urlencode
from download_tools import save_image


def get_the_latest_launch_photo(api_key=None):
    """Получает информацию о последнем запуске SpaceX."""
    url = 'https://api.spacexdata.com/v4/launches/latest'
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def extract_image_url(launch_data):
    """Извлекает URL изображения из данных о запуске."""
    return launch_data["links"]["patch"]["large"]

def download_spacex_image():
    """Скачивает изображение последнего запуска SpaceX и возвращает его содержимое в виде байтов."""
    launch_data = get_the_latest_launch_photo()
    image_url = extract_image_url(launch_data)

    if image_url:
        return save_image(image_url)
    return None


if __name__ == "__main__":
    image_bytes = download_spacex_image()

    



















