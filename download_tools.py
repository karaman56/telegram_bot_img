
import requests

def save_image(image_url):
    """Сохраняет изображение по указанному URL и возвращает его содержимое в байтах."""
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    return image_response.content


