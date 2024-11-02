import os
import requests
from dotenv import load_dotenv
from download_tools import save_image

SPACEX_IMAGES_DIRECTORY = "./spacex_images"

def fetch_spacex_latest_launch_info():
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    return response.json()

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









