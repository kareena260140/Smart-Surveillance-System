"""
=========================================================
telegram_bot.py

Telegram Notification Module
=========================================================
"""

import os
import requests

import config
from logger import logger


class TelegramBot:

    def __init__(self):

        self.token = config.BOT_TOKEN

        self.chat_id = config.CHAT_ID

        self.base_url = (
            f"https://api.telegram.org/bot{self.token}"
        )

    def send_message(self, message):

        url = f"{self.base_url}/sendMessage"

        payload = {
            "chat_id": self.chat_id,
            "text": message
        }

        try:

            response = requests.post(
                url,
                data=payload,
                timeout=10
            )

            if response.status_code == 200:

                logger.telegram_sent()

                return True

            logger.telegram_failed()

            return False

        except Exception as error:

            logger.error(str(error))

            return False

    def send_photo(self, image_path):

        if not os.path.exists(image_path):

            logger.error(
                "Image file not found."
            )

            return False

        url = f"{self.base_url}/sendPhoto"

        try:

            with open(image_path, "rb") as image:

                files = {
                    "photo": image
                }

                data = {
                    "chat_id": self.chat_id,
                    "caption": config.ALERT_MESSAGE
                }

                response = requests.post(
                    url,
                    data=data,
                    files=files,
                    timeout=20
                )

            if response.status_code == 200:

                logger.telegram_sent()

                return True

            logger.telegram_failed()

            return False

        except Exception as error:

            logger.error(str(error))

            return False

    def send_alert(self, image_path):

        self.send_message(config.ALERT_MESSAGE)

        self.send_photo(image_path)

    def connection_test(self):

        url = f"{self.base_url}/getMe"

        try:

            response = requests.get(
                url,
                timeout=10
            )

            if response.status_code == 200:

                logger.info(
                    "Telegram Bot Connected."
                )

                return True

            logger.error(
                "Telegram Bot Connection Failed."
            )

            return False

        except Exception as error:

            logger.error(str(error))

            return False
