#gp
import os
from dotenv import load_dotenv
from telegram import Bot

def load_config():
    """Загружает конфигурацию из переменных окружения."""
    load_dotenv()
    return {
        "TELEGRAM_BOT_TOKEN": os.getenv('TELEGRAM_BOT_TOKEN'),
        "TELEGRAM_CHANNEL_ID": os.getenv('TELEGRAM_CHANNEL_ID'),
    }

def publish_images_from_directory(telegram_bot, images_directory):
    """Публикует все изображения из указанного каталога в Telegram."""
    if not os.path.exists(images_directory):
        print(f"Каталог '{images_directory}' не существует.")
        return

    for image_file in os.listdir(images_directory):
        image_path = os.path.join(images_directory, image_file)
        if os.path.isfile(image_path):
            try:
                with open(image_path, 'rb') as image:
                    telegram_bot.send_photo(chat_id=os.getenv('TELEGRAM_CHANNEL_ID'), photo=image)
                    print(f"Изображение '{image_file}' успешно опубликовано.")
            except Exception as error:
                print(f"Не удалось опубликовать '{image_file}': {error}")
            finally:
                try:
                    os.remove(image_path)
                    print(f"{image_file} был удален после публикации.")
                except OSError as e:
                    print(f"Ошибка при удалении файла '{image_file}': {e}")

if __name__ == "__main__":
    config = load_config()
    telegram_bot = Bot(token=config['TELEGRAM_BOT_TOKEN'])
    publish_images_from_directory(telegram_bot, './some_directory')