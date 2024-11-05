import os
import telegram
from io import BytesIO

def publish_images_to_telegram(image_bytes, bot_token, chat_id):
    """Публикует изображение в Telegram."""
    bot = telegram.Bot(token=bot_token)
    image_file = BytesIO(image_bytes)  # Создаем объект BytesIO из байтов изображения
    image_file.name = 'image.png'  # Устанавливаем имя файла для Telegram
    bot.send_photo(chat_id=chat_id, photo=image_file)  # Отправляем изображение

if __name__ == "__main__":
    load_dotenv()
    bot_token_key = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id_key = os.getenv('TELEGRAM_CHANNEL_ID')









