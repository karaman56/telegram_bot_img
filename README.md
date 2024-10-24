# Телеграмм бот  для автоматического скачивания и публикации астрономических изображений


## Описание проекта

Телеграмм бот  для автоматического скачивания и публикации астрономических изображений — это скрипт на Python, который автоматически загружает изображения из различных источников, таких как NASA APOD (Astronomy Picture of the Day), EPIC и SpaceX, и публикует их в указанный Telegram-канал. Скрипт работает в цикле, позволяя пользователю настраивать интервал между публикациями.

## Требования к окружению

- Установленные зависимости: `python-telegram-bot`, `python-dotenv`, а также библиотеки для скачивания изображений

## Как установить

1. **Клонируйте репозиторий:**
`bash git clone https://github.com/karaman56/telegram_bot_img`

2. **Установите зависимости:**
bash pip install -r requirements.txt
#### В файле requirements.txt указаны следующие библиотеки:
`plaintext
python-dotenv==1.0.1
requests==2.31.0
urllib3==1.26.8
python-telegram-bot==13.0`

3. **Создайте файл `.env` и добавьте свои API ключи:**
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHANNEL_ID=@your_channel_id N
ASA_API_KEY=your_nasa_api_key
PUBLISH_INTERVAL=14400 # Время в секундах между публикациями
APOD_IMAGES_DIRECTORY=./apod_images
EPIC_IMAGES_DIRECTORY=./epic_images

## Примеры запуска скриптов

### Запуск основного скрипта для загрузки и публикации изображений

Чтобы запустить основной скрипт, используйте команду:
`bash python main.py`

### Запуск для загрузки изображений APOD

Вы можете запускать только загрузку изображений APOD:
`python # main.py def main(): download_apod_images('your_nasa_api_key', './apod_images', image_count=1)`
И запустите:
`bash python main.py`

### Запуск для загрузки изображений EPIC

Аналогично, чтобы загрузить изображения EPIC:
`python # main.py def main(): download_earth_images('your_nasa_api_key', './epic_images', max_image_count=1)`
И запустите:
`bash python main.py`

### Запуск для загрузки изображения SpaceX

Также можно загрузить изображение SpaceX:
`python # main.py def main(): download_spacex_image('./spacex_images')`
И запустите:
`bash python main.py`

## Примеры использования программного API

Просмотр доступа к функциям для скачивания изображений:
python from download_apod 
import download_apod_images from download_epic 
import download_earth_images from download_spacex 
import download_spacex_image
download_apod_images(api_key, './apod_images', image_count=1) 
download_earth_images(api_key, './epic_images', max_image_count=1) 
download_spacex_image('./spacex_images') ```

Каждая функция принимает обязательные параметры, такие как ваш API-ключ и путь для хранения изображений.

Заключение
```Этот проект является полезным инструментом для любителей астрономии и автоматизации публикаций в Telegram. Следуйте инструкциям выше, и вы сможете легко запустить его ```













