#ds
import requests
from general_functions import save_image

def fetch_spacex_image_url(launch_id=None):
    """Получает URL изображения SpaceX для указанного запуска."""
    return "https://example.com/path/to/spacex/image.jpg"  # Замените своими данными

def download_spacex_image(launch_id=None, download_directory='./spacex_images'):
    """Скачивает изображение SpaceX и сохраняет его в указанный каталог."""
    spacex_image_url = fetch_spacex_image_url(launch_id)
    if spacex_image_url:
        image_filename = "spacex_image.jpg"
        save_image(spacex_image_url, download_directory, image_filename)