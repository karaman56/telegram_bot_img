import os
from telegram import Bot

def publish_images_to_telegram(directory, bot_token, chat_id):
    bot = Bot(token=bot_token)
    if not os.listdir(directory):
        print(f"Нет изображений для публикации в {directory}.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            with open(file_path, 'rb') as file:
                bot.send_photo(chat_id, photo=file)
                os.remove(file_path)
                print(f"Опубликовано изображение в Telegram: {file_path}")
        except Exception as error:
            print(f"Ошибка при публикации изображения в Telegram: {error}")

