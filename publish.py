import os
import telegram
from dotenv import load_dotenv

def publish_images_to_telegram(image_folder, bot_token, chat_id):
    bot = telegram.Bot(token=bot_token)
    for image_name in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_name)
        with open(image_path, 'rb') as f:
            bot.send_photo(chat_id=chat_id, photo=f)
        print(f"Опубликовано изображение: {image_name}")

if __name__ == "__main__":
    load_dotenv()
    bot_token_key = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id_key = os.getenv('TELEGRAM_CHANNEL_ID')

    publish_images_to_telegram('./apod_images', bot_token_key, chat_id_key)
    publish_images_to_telegram('./epic_images', bot_token_key, chat_id_key)
    publish_images_to_telegram('./spacex_images', bot_token_key, chat_id_key)






