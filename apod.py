import os
import requests
from urllib.parse import urlencode
import time

APOD_IMAGES_DIRECTORY = "./apod_images"


def build_apod_url(api_key):
    params = {'api_key': api_key}
    return 'https://api.nasa.gov/planetary/apod?' + urlencode(params)


def fetch_apod_image_info(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_image(image_url, directory, prefix):
    try:
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        extension = image_url.split('.')[-1]
        if extension not in ['jpg', 'jpeg', 'png', 'gif']:
            raise ValueError("URL не содержит известного расширения")

        file_path = f"{directory}/{prefix}_{time.time()}.{extension}"
        with open(file_path, 'wb') as file:
            file.write(image_response.content)
        return file_path
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при загрузке изображения: {error}")
        return None

def download_apod_images(count=1, api_key=None):
    if not os.path.exists(APOD_IMAGES_DIRECTORY):
        os.makedirs(APOD_IMAGES_DIRECTORY)
    for _ in range(count):
        url = build_apod_url(api_key)
        apod_image_info = fetch_apod_image_info(url)
        if apod_image_info and 'url' in apod_image_info:
            image_url = apod_image_info['url']
            print(f"APOD Image URL: {image_url}")
            file_path = save_image(image_url, APOD_IMAGES_DIRECTORY, "apod")
            if file_path:
                print(f"Скачано изображение APOD: {file_path}")
        else:
            print("Нет данных для APOD.")

