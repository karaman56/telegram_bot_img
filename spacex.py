import os
import requests
from dotenv import load_dotenv

SPACEX_IMAGES_DIRECTORY = "./spacex_images"

def fetch_spacex_latest_launch_info():
    try:
        response = requests.get('https://api.spacexdata.com/v4/launches/latest')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при запросе к SpaceX API: {error}")
        return None

def save_image(image_url, directory, prefix):
    try:
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        extension = image_url.split('.')[-1]
        file_path = f"{directory}/{prefix}_{time.time()}.{extension}"
        with open(file_path, 'wb') as file:
            file.write(image_response.content)
        return file_path
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при загрузке изображения: {error}")
        return None

def download_spacex_image():
    if not os.path.exists(SPACEX_IMAGES_DIRECTORY):
        os.makedirs(SPACEX_IMAGES_DIRECTORY)

    spacex_latest_launch_info = fetch_spacex_latest_launch_info()
    if spacex_latest_launch_info:
        image_url = spacex_latest_launch_info["links"]["patch"]["large"]
        file_path = save_image(image_url, SPACEX_IMAGES_DIRECTORY, spacex_latest_launch_info.get("name", "default_mission").replace(" ", "_"))
        if file_path:
            print(f"Скачано изображение SpaceX: {file_path}")

if __name__ == "__main__":
    load_dotenv()
    download_spacex_image()







