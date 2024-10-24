#gf
import requests
import os

def save_image(image_url, download_directory, filename):
    """Скачивает изображение по URL и сохраняет его в заданном каталоге."""
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        os.makedirs(download_directory, exist_ok=True)

        image_path = os.path.join(download_directory, filename)
        with open(image_path, 'wb') as file:
            file.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе изображения '{image_url}': {e}")
    except OSError as e:
        print(f"Ошибка при сохранении изображения '{filename}': {e}")