import requests
from download_tools import save_image


def get_the_latest_launch_photo():
    """Получает информацию о последнем запуске SpaceX."""
    url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main():
    """Основная функция программы."""
    launch_data = get_the_latest_launch_photo()
    image_url = launch_data["links"]["patch"]["large"]

    if image_url:
        image_bytes = save_image(image_url)
       


if __name__ == "__main__":
    main()



    



















