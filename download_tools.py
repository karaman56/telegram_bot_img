import os
import requests
import time

def save_image(image_url, directory, prefix):
    """Сохраняет изображение по указанному URL."""
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    extension = image_url.split('.')[-1]
    file_path = os.path.join(directory, f"{prefix}_{time.time()}.{extension}")
    with open(file_path, 'wb') as file:
        file.write(image_response.content)
    return file_path

