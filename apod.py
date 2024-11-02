import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
from download_tools import save_image  

APOD_IMAGES_DIRECTORY = "./apod_images"

def get_apod_images(api_key, count):
    params = {
        'api_key': api_key,
        'count': count
    }
    url = 'https://api.nasa.gov/planetary/apod?' + urlencode(params)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def download_apod_images(count=1, api_key=None):
    os.makedirs(APOD_IMAGES_DIRECTORY, exist_ok=True)
    apod_images = get_apod_images(api_key, count)
    for apod_image in apod_images:
        if apod_image and 'url' in apod_image:
            image_url = apod_image['url']
            print(f"APOD Image URL: {image_url}")
            file_path = save_image(image_url, APOD_IMAGES_DIRECTORY, "apod")
            if file_path:
                print(f"Скачано изображение APOD: {file_path}")
        else:
            print("Нет данных для APOD.")

if __name__ == "__main__":
    load_dotenv()
    api_key_nasa = os.getenv('NASA_API_KEY')
    download_apod_images(count=5, api_key=api_key_nasa)


















