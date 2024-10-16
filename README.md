# NASA and SpaceX Image 

## Этот проект представляет собой программу, которая автоматически извлекает изображения из NASA и SpaceX и публикует их в указанном канале Telegram. Он нацелен на предоставление пользователям интересных астрономических и космических изображений каждый день.

### Основные функции

Извлечение изображений из NASA: 
Программа обращается к различным API NASA для получения изображений. В частности, она загружает Астрономическую картину дня (APOD) и изображения EPIC (Earth Polychromatic Imaging Camera).
Извлечение изображений SpaceX: Программа также получает изображения с последних запусков SpaceX, обеспечивая публикацию интересных космических событий.
Автоматизация публикации: Изображения автоматически загружаются в указанный канал Telegram через заданные промежутки времени.

### Установка:
Клонирование репозитория: Сначала клонируйте этот репозиторий на ваш локальный компьютер:
```bash
git clone <URL_репозитория>
cd <имя_папки>
```
#### Установка зависимостей: 
  Убедитесь, что у вас установлен Python, затем установите необходимые библиотеки:
```bash
pip install -r requirements.txt
```
#### В файле requirements.txt указаны следующие библиотеки:
`plaintext
python-dotenv==1.0.1
requests==2.31.0
urllib3==1.26.8
python-telegram-bot==13.0
`

#### Настройка переменных окружения: Создайте файл `.env` в корневой директории проекта и добавьте в него следующие строки:
```plaintext
NASA_API_KEY=<ваш_NASA_API_ключ>
TELEGRAM_BOT_TOKEN=<ваш_ТГ_бот_токен>
TELEGRAM_CHANNEL_ID=<ваш_ТГ_канал_ID>
PUBLISH_INTERVAL=<интервал_публикации_в_секундах>
APOD_IMAGES_DIRECTORY=./apod_images
EPIC_IMAGES_DIRECTORY=./epic_images
```

Замените значения на ваши. `PUBLISH_INTERVAL` — время в секундах между публикациями изображений (по умолчанию 14400 секунд).

#### Запуск программы
Для запуска программы используйте команду: `python main.py`
После этого программа начнёт извлечение изображений и публикацию их в ваш Telegram-канал.

#### Проверка работы
Чтобы проверить, что программа работает корректно:
- Удостоверьтесь, что ваш бот в Telegram создан и добавлен в ваш канал и имеет разрешение на публикацию сообщений (назначен администратором канала).
- После запуска программы в течение указанного интервала времени должны появляться новые сообщения в канале с изображениями из NASA и SpaceX.
- Проверьте, что все полученные изображения правильно загружаются в соответствующие директории `(./apod_images и ./epic_images)`.
Если вы видите изображения в вашем канале Telegram, значит, программа работает правильно!

### Заключение
Этот проект – замечательный способ следить за астрономическими событиями и достижениями в космической отрасли. Он автоматизирует процесс извлечения и публикации изображений, позволяя вам наслаждаться ими без лишних усилий.
