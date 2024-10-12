import os
from common import fetch_images_from_apod, download_image, load_environment

def main():
    load_environment()
    save_directory = os.getenv('APOD_IMAGES_DIRECTORY', './apod_images')
    os.makedirs(save_directory, exist_ok=True)

    image_urls = fetch_images_from_apod(count=5)
    if not image_urls:
        print("Нет доступных изображений для скачивания из APOD.")
        return

    for index, image_url in enumerate(image_urls, start=1):
        download_image(image_url, save_directory, f"apod_image_{index}.jpg")

if __name__ == "__main__":
    main()

