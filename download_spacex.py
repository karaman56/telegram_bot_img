#ds
import requests
import os
from general_functions import save_image


def fetch_spacex_image_url(launch_id=None):
    """Получает URL изображения SpaceX для указанного запуска."""

    return "https://example.com/path/to/spacex/image.jpg"  # Замените своим кодом


def download_spacex_image(launch_id=None, download_directory='./spacex_images'):
    """Скачивает изображение SpaceX и сохраняет его в каталог."""
    spacex_image_url = fetch_spacex_image_url(launch_id)
    if spacex_image_url:
        save_image(spacex_image_url, download_directory, "spacex_image.jpg")


if __name__ == "__main__":

    pass