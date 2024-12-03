import os
import requests
from dotenv import load_dotenv
from download_tools import save_image

def get_apod_images(api_key, count=1):
    """Получает данные APOD из NASA API и сохраняет изображения на диск."""
    params = {
        'api_key': api_key,
        'count': count
    }
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    response.raise_for_status()
    apod_images = response.json()

    for image in apod_images:
        if 'url' in image:
            save_image(image['url'])

def main():
    load_dotenv()
    api_key_nasa = os.getenv('NASA_API_KEY')
    get_apod_images(api_key=api_key_nasa, count=1)

if __name__ == "__main__":
    main()























