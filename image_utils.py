# image_utils.py
import os
import requests



def download_image(url, directory, filename):
    """Downloads an image from the given URL to a specified directory."""
    try:
        print(f"Начинаю загрузку изображения: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Вызывает ошибку для HTTP ошибок

        # Убедитесь, что контент - это изображение
        content_type = response.headers.get('Content-Type')
        if not content_type or not content_type.startswith('image/'):
            print(f"Ошибка: URL не ведет к изображению: {url}, Content-Type: {content_type}")
            return

        # Создание директории, если она не существует
        os.makedirs(directory, exist_ok=True)
        image_path = os.path.join(directory, filename)

        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f"Изображение загружено: {image_path}")

    except requests.exceptions.HTTPError as err:
        print(f"Ошибка при загрузке изображения: {url} - {err}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")