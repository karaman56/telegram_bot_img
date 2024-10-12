import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from urllib.parse import urlencode

def load_environment():
    load_dotenv()

# Константы для конфигурации
NASA_API_KEY = os.getenv('NASA_API_KEY')
if NASA_API_KEY is None:
    raise ValueError("Отсутствует NASA_API_KEY в переменных окружения.")

def download_image(image_url, save_directory, filename, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
            file_path = os.path.join(save_directory, filename)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Изображение загружено: {file_path}")
            return
        except requests.RequestException as e:
            print(f"Ошибка при загрузке изображения {image_url}: {e}. Попытка {attempt + 1} из {retries}.")
    print(f"Не удалось загрузить изображение: {image_url}")

def construct_nasa_api_url(endpoint, params):
    base_url = f"https://api.nasa.gov{endpoint}"
    return f"{base_url}?{urlencode(params)}"

def fetch_images_from_epic(count=5):
    endpoint = "/EPIC/api/natural/images"
    params = {"api_key": NASA_API_KEY}
    url = construct_nasa_api_url(endpoint, params)

    response = requests.get(url)
    response.raise_for_status()
    epic_image_data = response.json()

    image_urls = []
    for item in epic_image_data[:count]:
        date_time_str = item['date']
        date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        date_str = date_time.strftime("%Y/%m/%d")
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date_str}/png/{item['image']}.png"
        image_urls.append(image_url)

    return image_urls

def fetch_images_from_apod(count=5):
    endpoint = "/planetary/apod"
    params = {"api_key": NASA_API_KEY, "count": count}
    url = construct_nasa_api_url(endpoint, params)

    response = requests.get(url)
    response.raise_for_status()
    apod_image_data = response.json()

    image_urls = [item['url'] for item in apod_image_data if item['media_type'] == 'image']
    return image_urls