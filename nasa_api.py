# nasa_api.py
import requests
from urllib.parse import urlencode
from datetime import datetime
import os

NASA_API_KEY = os.getenv('NASA_API_KEY')


def check_image_availability(url):
    """Check if the image is available at the given URL."""
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return True
        else:
            print(f"Image not found: {url} - Status Code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error checking image availability: {e}")
        return False


def fetch_images(endpoint, params):
    """Fetches data from the specified NASA API endpoint."""
    base_url = "https://api.nasa.gov"
    query_string = urlencode(params)
    url = f"{base_url}{endpoint}?{query_string}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_apod_images(count=5):
    """Fetches Astronomy Picture of the Day (APOD) images from NASA API."""
    endpoint = "/planetary/apod"
    params = {"api_key": NASA_API_KEY, "count": count}
    apod_image_data = fetch_images(endpoint, params)
    image_urls = [item['url'] for item in apod_image_data if item['media_type'] == 'image']
    return image_urls

def fetch_epic_images(count=5):
    """Fetches EPIC images from NASA API."""
    endpoint = "/EPIC/api/natural/images"
    params = {"api_key": NASA_API_KEY}
    epic_image_data = fetch_images(endpoint, params)

    image_urls = []
    for item in epic_image_data[:count]:
        date_time_str = item['date']
        date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        date_str = date_time.strftime("%Y/%m/%d")

        # Формирование URL для изображения
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date_str}/png/{item['image']}.png"

        # Проверка доступности изображения
        if check_image_availability(image_url):
            image_urls.append(image_url)

    return image_urls