#epic
import requests
import os
from general_functions import is_image_available, save_image


def fetch_epic_image_urls(api_key, count=5):
    """Получает URL изображений Земли из EPIC."""
    endpoint = "/EPIC/api/natural/images"
    params = {"api_key": api_key}

    response = requests.get(f"https://api.nasa.gov{endpoint}", params=params)
    response.raise_for_status()
    epic_images_data = response.json()

    available_image_urls = []
    for image_item in epic_images_data[:count]:
        # Извлечение формата даты
        date_time_str = image_item['date']
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date_time_str[:10].replace('-', '/')}/png/{image_item['image']}.png"
        if is_image_available(image_url):
            available_image_urls.append(image_url)

    return available_image_urls


def download_epic_images(api_key, download_directory, count=5):
    """Скачивает EPIC изображения и сохраняет их в каталог."""
    epic_image_urls = fetch_epic_image_urls(api_key, count)

    for index, image_url in enumerate(epic_image_urls, start=1):
        save_image(image_url, download_directory, f"epic_image_{index}.png")


if __name__ == "__main__":
