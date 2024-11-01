

# Проект: Скачивание и публикация изображений из NASA и SpaceX

Этот проект предназначен для автоматического скачивания изображений из NASA (APOD и EPIC) и SpaceX, а также их публикации в Telegram. Он использует API NASA и SpaceX, а также библиотеку для работы с Telegram.

## Установка

Для начала вам нужно установить необходимые зависимости. Убедитесь, что у вас установлен Python 3.6 или выше. Затем выполните следующие шаги:

1. Клонируйте репозиторий проекта:

```bash
git clone https://github.com/karaman56/telegram_bot_img
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
- `publish.py`: скрипт, который используется  для публикации изображений.
- `main.py`: основной файл для запуска проекта.

### 1. `apod.py`

Этот файл содержит функции для работы с API NASA APOD. Он включает в себя:

- **Построение URL для APOD**: Функция `build_apod_url(api_key)` создает URL для запроса к API.
- **Получение информации об изображении APOD**: Функция `fetch_apod_image_info(url)` делает запрос к API и возвращает информацию об изображении.
- **Сохранение изображения**: Функция `save_image(image_url, directory, prefix)` загружает изображение и сохраняет его в указанной директории.
- **Скачивание изображений APOD**: Функция `download_apod_images(count, api_key)` скачивает заданное количество изображений.

Пример функции для построения URL для APOD:

```python
def build_apod_url(api_key): params = {'api_key': api_key}
return 'https://api.nasa.gov/planetary/apod?' + urlencode(params)
```

### 2. `epic.py`
Этот файл содержит функции для работы с API NASA EPIC. Он включает в себя:
<br>- Построение URL для EPIC: Функция `build_epic_url(api_key)` создает URL для запроса к API. 
<br>- Получение информации об изображениях EPIC: Функция `fetch_epic_image_info(url)` делает запрос к API и возвращает информацию об изображениях. 
<br>- Скачивание изображений EPIC: Функция `download_epic_images(count, api_key)` скачивает заданное количество изображений.

#### Пример функции для получения информации об изображениях EPIC
```python
def fetch_epic_image_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при запросе к EPIC API: {error}")
        return []
```
        
### 3. spacex.py

Этот файл содержит функции для работы с API SpaceX. Он включает в себя:

- Получение информации о последнем запуске SpaceX: Функция `fetch_spacex_latest_launch_info()` делает запрос к API и возвращает информацию о последнем запуске.
- Скачивание изображения SpaceX: Функция `download_spacex_image()` скачивает изображение последнего запуска.

#### Пример функции для получения информации о последнем запуске SpaceX
```python
 def fetch_spacex_latest_launch_info(): try:

response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    return response.json()
except requests.exceptions.RequestException as error:
    print(f"Ошибка при запросе к SpaceX API: {error}")
    return None
```

### 4. publish.py

Этот файл используеться для публикации изображений, скачанных из других источников.

### 6. main.py

Это основной файл, который запускает весь процесс. Он использует функции из других файлов для скачивания изображений и их публикации в Telegram.


## Заключение

Этот проект позволяет автоматически скачивать и публиковать изображения из NASA и SpaceX, что может быть полезно для любителей астрономии и космоса. 


        
        










