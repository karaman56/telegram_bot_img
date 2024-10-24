import os

def publish_images_from_directory(telegram_bot, images_directory):
    """Публикует все изображения из указанного каталога в Telegram."""
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
                except OSError as e:
                    print(f"Ошибка при удалении файла '{image_file}': {e}")