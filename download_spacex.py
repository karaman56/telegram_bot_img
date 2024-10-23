#ds
import requests
import os
from general_functions import save_image


def fetch_spacex_image_url(launch_id=None):
    """Получает URL изображения SpaceX для указанного запуска."""
    # Ваш код для получения URL из API SpaceX
    return "https://example.com/path/to/spacex/image.jpg"  # Замените своими данными


def download_spacex_image(launch_id=None, download_directory='./spacex_images'):
    """Скачивает изображение SpaceX и сохраняет его в указанный каталог."""
    spacex_image_url = fetch_spacex_image_url(launch_id)
    if spacex_image_url:
        image_filename = "spacex_image.jpg"
        save_image(spacex_image_url, download_directory, image_filename)


if __name__ == "__main__":
    # Добавьте логику для обработки командной строки, если нужно
    pass