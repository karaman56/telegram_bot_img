

# Проект: Скачивание и публикация изображений из NASA и SpaceX

Этот проект предназначен для автоматического скачивания изображений из NASA (APOD и EPIC) и SpaceX, а также их публикации в Telegram. Он использует API NASA и SpaceX, а также библиотеку для работы с Telegram.

## Установка

Для начала вам нужно установить необходимые зависимости. Убедитесь, что у вас установлен Python 3.6 или выше. Затем выполните следующие шаги:

1. Клонируйте репозиторий проекта:

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

2. Установите необходимые библиотеки:

```bash
pip install requests python-telegram-bot python-dotenv
```

3. Создайте файл `.env` в корневом каталоге проекта и добавьте в него ваши API ключи:

```plaintext
NASA_API_KEY=ваш_ключ_NASA
TELEGRAM_BOT_TOKEN=ваш_токен_бота
TELEGRAM_CHAT_ID=ваш_chat_id
```

## Структура проекта

Проект состоит из нескольких файлов, каждый из которых отвечает за определенные функции:

- `apod.py`: функции для работы с API NASA APOD.
- `epic.py`: функции для работы с API NASA EPIC.
- `spacex.py`: функции для работы с API SpaceX.
- `telegram.py`: функции для публикации изображений в Telegram.
- `main.py`: основной файл для запуска проекта.

## Описание файлов

### 1. `apod.py`

Этот файл содержит функции для работы с API NASA APOD. Он включает в себя:

- **Построение URL для APOD**: Функция `build_apod_url(api_key)` создает URL для запроса к API.
- **Получение информации об изображении APOD**: Функция `fetch_apod_image_info(url)` делает запрос к API и возвращает информацию об изображении.
- **Сохранение изображения**: Функция `save_image(image_url, directory, prefix)` загружает изображение и сохраняет его в указанной директории.
- **Скачивание изображений APOD**: Функция `download_apod_images(count, api_key)` скачивает заданное количество изображений.

Пример функции для построения URL для APOD
```python
def build_apod_url(api_key): params = {'api_key': api_key}
return 'https://api.nasa.gov/planetary/apod?' + urlencode(params)
```
<br>
### 2. `epic.py` <br><br> Этот файл содержит функции для работы с API NASA EPIC. Он включает в себя:<br><br>- **Построение URL для EPIC**: Функция `build_epic_url(api_key)` создает URL для запроса к API.<br>- 
**Получение информации об изображениях EPIC**: Функция `fetch_epic_image_info(url)` делает запрос к API и возвращает информацию об изображениях.<br>- 
**Скачивание изображений EPIC**: Функция `download_epic_images(count, api_key)` скачивает заданное количество изображений.<br><br>```python<br>

# Пример функции для получения информации об изображениях EPIC
def fetch_epic_image_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при запросе к EPIC API: {error}")
        return []
        
### 3. spacex.py

Этот файл содержит функции для работы с API SpaceX. Он включает в себя:

- Получение информации о последнем запуске SpaceX: Функция fetch_spacex_latest_launch_info() делает запрос к API и возвращает информацию о последнем запуске.
- Скачивание изображения SpaceX: Функция download_spacex_image() скачивает изображение последнего запуска.

# Пример функции для получения информации о последнем запуске SpaceX
```python
 def fetch_spacex_latest_launch_info(): try:

response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    return response.json()
except requests.exceptions.RequestException as error:
    print(f"Ошибка при запросе к SpaceX API: {error}")
    return None
```
<br>### 4. `telegram.py`<br><br>Этот файл содержит функции для публикации изображений в Telegram. Он включает в себя:<br><br>- **Публикация изображений в Telegram**: Функция `publish_images_to_telegram(directory, bot_token, chat_id)` отправляет изображения из указанной директории в Telegram.<br><br>
```python<br># Пример функции для публикации изображений в Telegram
def publish_images_to_telegram(directory, bot_token, chat_id):
    bot = Bot(token=bot_token)
    if not os.listdir(directory):
        print(f"Нет изображений для публикации в {directory}.")
        return
```
### 5. main.py

Это основной файл, который запускает весь процесс. Он использует функции из других файлов для скачивания изображений и их публикации в Telegram.

```python
# Пример основного цикла в main.py while True: try: download_apod_images(count=args.count, api_key=API_KEY) download_epic_images(count=args.count, api_key=API_KEY) download_spacex_image()

    publish_images_to_telegram(APOD_IMAGES_DIRECTORY, BOT_TOKEN, CHAT_ID)
    publish_images_to_telegram(EPIC_IMAGES_DIRECTORY, BOT_TOKEN, CHAT_ID)
    publish_images_to_telegram(SPACEX_IMAGES_DIRECTORY, BOT_TOKEN, CHAT_ID)

    print('Изображения успешно опубликованы. Ждем перед следующей итерацией.')
except Exception as error:
    print(f"Ошибка в основном цикле: {error}")
<br>## Запуск проекта<br><br>Чтобы запустить проект, выполните следующую команду в терминале:<br><br>```bash<br>python main.py --count 3 --interval 14400
```

Здесь `--count` указывает количество изображений для загрузки, а `--interval` — интервал публикации в секундах.

## Заключение

Этот проект позволяет автоматически скачивать и публиковать изображения из NASA и SpaceX, что может быть полезно для любителей астрономии и космоса. 


        
        










