
import os
import telegram
from io import BytesIO
from dotenv import load_dotenv

def publish_images_to_telegram(image_bytes, bot_token, chat_id):
    """Публикует изображение в Telegram."""
    bot = telegram.Bot(token=bot_token)
    image_file = BytesIO(image_bytes)
    image_file.name = 'image.png'
    bot.send_photo(chat_id=chat_id, photo=image_file)

if __name__ == "__main__":
    load_dotenv()
    bot_token_key = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id_key = os.getenv('TELEGRAM_CHANNEL_ID')











