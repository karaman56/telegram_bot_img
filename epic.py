import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
import time  # Не забудьте импортировать time, так как он используется в save_image

EPIC_IMAGES_DIRECTORY = "./epic_images"

    
def fetch_epic_image_info(url):
    params = {'api_key': api_key}
    url = 'https://api.nasa.gov/EPIC/api/natural/all?' + urlencode(params)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_image(image_url, directory, prefix):
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    extension = image_url.split('.')[-1]
    file_path = f"{directory}/{prefix}_{time.time()}.{extension}"
    with open(file_path, 'wb') as file:
        file.write(image_response.content)
    return file_path


def download_epic_images(count=1, api_key=None):
    os.makedirs(EPIC_IMAGES_DIRECTORY, exist_ok=True)
    url = build_epic_url(api_key)
    epic_image_info_list = fetch_epic_image_info(url)[:count]
    for item in epic_image_info_list:
        date_str = item['date'].split(' ')[0].replace('-', '/')
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date_str}/png/{item['image']}.png"
        print(f"EPIC Image URL: {image_url}")
        file_path = save_image(image_url, EPIC_IMAGES_DIRECTORY, f"epic_{date_str}")
        if file_path:
            print(f"Скачано изображение EPIC: {file_path}")

if __name__ == "__main__":
    load_dotenv()
    api_key_nasa = os.getenv('NASA_API_KEY')
    download_epic_images(count=3, api_key=api_key_nasa)








