import os
from common import fetch_images_from_epic, download_image, load_environment

def main():
    load_environment()
    save_directory = os.getenv('EPIC_IMAGES_DIRECTORY', './epic_images')
    os.makedirs(save_directory, exist_ok=True)

    image_urls = fetch_images_from_epic(count=5)
    if not image_urls:
        print("Нет доступных изображений для скачивания из EPIC.")
        return

    for index, image_url in enumerate(image_urls, start=1):
        download_image(image_url, save_directory, f"epic_image_{index}.png")

if __name__ == "__main__":
    main()