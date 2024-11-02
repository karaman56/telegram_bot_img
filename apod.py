import os
import requests
from urllib.parse import urlencode
import time
from dotenv import load_dotenv

APOD_IMAGES_DIRECTORY = "./apod_images"

def get_apod_image(api_key):
    params = {'api_key': api_key}
    url = 'https://api.nasa.gov/planetary/apod?' + urlencode(params)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_image(image_url, directory, prefix):
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    extension = image_url.split('.')[-1]
    if extension not in ['jpg', 'jpeg', 'png', 'gif']:
        raise ValueError("URL не содержит известного расширения")
    file_path = f"{directory}/{prefix}_{time.time()}.{extension}"
    with open(file_path, 'wb') as file:
        file.write(image_response.content)
    return file_path

def download_apod_images(count=1, api_key=None):
    os.makedirs(APOD_IMAGES_DIRECTORY, exist_ok=True)
    for _ in range(count):
        apod_image_save = get_apod_image(api_key)
        if apod_image_save and 'url' in apod_image_data:
            image_url = apod_image_save['url']
            print(f"APOD Image URL: {image_url}")
            file_path = save_image(image_url, APOD_IMAGES_DIRECTORY, "apod")
            if file_path:
                print(f"Скачано изображение APOD: {file_path}")
        else:
            print("Нет данных для APOD.")

if __name__ == "__main__":
    load_dotenv()
    api_key_nasa = os.getenv('NASA_API_KEY')
    download_apod_images(count=3, api_key=api_key_nasa)












