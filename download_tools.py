
import requests

def save_image(image_url):
    """Сохраняет изображение по указанному URL в папку images и возвращает его содержимое в байтах."""
    image_response = requests.get(image_url)
    image_response.raise_for_status()

    filename = image_url.split("/")[-1]
    """Получаем избражение."""
    with open(f'./images/{filename}', 'wb') as image_file:
        image_file.write(image_response.content)
    return image_response.content


