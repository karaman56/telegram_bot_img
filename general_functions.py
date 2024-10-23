#gf
import requests
import os

def is_image_available(image_url):
    """Проверяет доступность изображения по URL."""
    response = requests.head(image_url)
    return response.status_code == 200

def save_image(image_url, download_directory, filename):
    """Скачивает изображение по URL и сохраняет его в заданном каталоге."""
    response = requests.get(image_url)
    response.raise_for_status()
    os.makedirs(download_directory, exist_ok=True)
    image_path = os.path.join(download_directory, filename)
    with open(image_path, 'wb') as file:
        file.write(response.content)