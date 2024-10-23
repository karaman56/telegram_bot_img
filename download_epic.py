#epic
import requests
from general_functions import is_image_available, save_image

def fetch_epic_image_urls(api_key, max_image_count=5):
    """Получает URL изображений Земли из EPIC."""
    endpoint = "/EPIC/api/natural/images"
    params = {"api_key": api_key}

    response = requests.get(f"https://api.nasa.gov{endpoint}", params=params)
    response.raise_for_status()

    epic_image_response = response.json()
    return [
        f"https://epic.gsfc.nasa.gov/archive/natural/{item['date'][:10].replace('-', '/')}/png/{item['image']}.png"
        for item in epic_image_response[:max_image_count]
    ]

def download_epic_images(image_urls, download_directory):
    """Скачивает EPIC изображения и сохраняет их в указанный каталог."""
    for index, image_url in enumerate(image_urls, start=1):
        if is_image_available(image_url):
            image_filename = f"epic_image_{index}.png"
            save_image(image_url, download_directory, image_filename)