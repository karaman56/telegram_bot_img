import os
import requests
from dotenv import load_dotenv
from download_tools import save_image

SPACEX_IMAGES_DIRECTORY = "./spacex_images"

def get_the_latest_launch_photo():
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    return response.json()

def download_spacex_image():
    the_latest_launch_photo = get_the_latest_launch_photo()

    if not the_latest_launch_photo:
        return None
    image_url = the_latest_launch_photo["links"]["patch"]["large"]
    if not image_url:
        return None
    return save_image(image_url)

if __name__ == "__main__":
    image_bytes = download_spacex_image()
    if image_bytes:
        print("Скачано изображение SpaceX.")













