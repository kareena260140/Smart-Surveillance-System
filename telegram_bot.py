"""
telegram_bot.py
Sends Telegram notifications with images.
"""

import os
import requests
import config


class TelegramBot:

    def __init__(self):
        self.token = config.BOT_TOKEN
        self.chat_id = config.CHAT_ID

    def send_message(self, message):

        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        data = {
            "chat_id": self.chat_id,
            "text": message
        }

        try:
            requests.post(url, data=data)
        except Exception as error:
            print("Telegram Message Error:", error)

    def send_photo(self, image_path):

        if not os.path.exists(image_path):
            print("Image not found.")
            return

        url = f"https://api.telegram.org/bot{self.token}/sendPhoto"

        try:
            with open(image_path, "rb") as image:

                files = {
                    "photo": image
                }

                data = {
                    "chat_id": self.chat_id,
                    "caption": config.ALERT_MESSAGE
                }

                requests.post(
                    url,
                    files=files,
                    data=data
                )

        except Exception as error:
            print("Telegram Photo Error:", error)
