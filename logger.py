"""
=========================================================
logger.py

Handles logging for Smart Surveillance System
=========================================================
"""

import logging
import os
import config


class SurveillanceLogger:

    def __init__(self):

        self.logger = logging.getLogger(config.PROJECT_NAME)

        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                config.LOG_FILE
            )

            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

            self.logger.addHandler(console_handler)

    def info(self, message):

        self.logger.info(message)

    def warning(self, message):

        self.logger.warning(message)

    def error(self, message):

        self.logger.error(message)

    def critical(self, message):

        self.logger.critical(message)

    def system_started(self):

        self.info("=" * 60)
        self.info("Smart Surveillance System Started")
        self.info("=" * 60)

    def system_stopped(self):

        self.info("=" * 60)
        self.info("System Shutdown")
        self.info("=" * 60)

    def camera_connected(self):

        self.info("Camera initialized successfully.")

    def camera_failed(self):

        self.error("Unable to initialize camera.")

    def motion_detected(self):

        self.warning("Motion detected.")

    def face_detected(self, count):

        self.warning(f"Face detected : {count}")

    def image_saved(self, path):

        self.info(f"Image saved : {path}")

    def telegram_sent(self):

        self.info("Telegram notification sent.")

    def telegram_failed(self):

        self.error("Telegram notification failed.")

    def model_loaded(self):

        self.info("Haar Cascade model loaded.")

    def model_failed(self):

        self.error("Unable to load Haar Cascade model.")

    def application_error(self, error):

        self.critical(str(error))


logger = SurveillanceLogger()
