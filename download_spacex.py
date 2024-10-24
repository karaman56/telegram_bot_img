#ds
import requests
from general_functions import save_image


def fetch_spacex_image_url(launch_id=None):
    """Получает URL изображения SpaceX для указанного запуска или для последнего запуска, если ID не указан."""
    base_url = 'https://api.spacexdata.com/v5/launches'
    url = f"{base_url}/{launch_id}" if launch_id else f"{base_url}/latest"
    response = requests.get(url)
    response.raise_for_status()
    launch_data = response.json()
    image_url = launch_data['links'].get('patch', {}).get('large', None)
    return image_url



def download_spacex_image(launch_id=None, download_directory='./spacex_images'):
    """Скачивает изображение SpaceX и сохраняет его в указанный каталог."""
    spacex_image_url = fetch_spacex_image_url(launch_id)

    if spacex_image_url:
        image_filename = "spacex_image.jpg"
        save_image(spacex_image_url, download_directory, image_filename)
    else:
        print("Не удалось получить URL изображения SpaceX.")