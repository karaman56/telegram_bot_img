#epic
import requests
from urllib.parse import urlencode
from general_functions import save_image

def fetch_earth_image_urls(api_key, max_image_count=1):
    """Получает URL изображений Земли из EPIC."""
    endpoint = "/EPIC/api/natural/images"
    params = {"api_key": api_key}
    query_string = urlencode(params)
    response = requests.get(f"https://api.nasa.gov{endpoint}?{query_string}")
    response.raise_for_status()
    epic_image_data = response.json()
    return [
        f"https://epic.gsfc.nasa.gov/archive/natural/{item['date'][:10].replace('-', '/')}/png/{item['image']}.png"
        for item in epic_image_data[:max_image_count]
    ]

def download_earth_images(api_key, download_directory, max_image_count=1):
    """Скачивает изображения Земли и сохраняет их в указанный каталог."""
    image_urls = fetch_earth_image_urls(api_key, max_image_count)
    for index, image_url in enumerate(image_urls, start=1):
        image_filename = f"epic_image_{index}.png"
        save_image(image_url, download_directory, image_filename)