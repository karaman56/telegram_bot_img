# spacex_api.py
import requests
from urllib.parse import urlencode


def fetch_spacex_image(launch_id=None):
    """Fetches an image from SpaceX launches."""
    base_url = 'https://api.spacexdata.com/v5/launches'
    params = {}

    if launch_id:
        params['id'] = launch_id

    query_string = urlencode(params)
    url = f"{base_url}/latest?{query_string}" if not launch_id else f"{base_url}/{launch_id}"

    response = requests.get(url)
    response.raise_for_status()
    launch_data = response.json()
    image_url = launch_data['links']['patch']['large']

    if not image_url:
        print("Изображение SpaceX отсутствует.")
        return None

    return image_url