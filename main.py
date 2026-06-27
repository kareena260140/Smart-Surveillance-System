"""
=========================================================
main.py

Smart Surveillance System
Main Application
=========================================================
"""

import cv2
import time

import config

from logger import logger
from camera import Camera
from motion import MotionDetector
from face_detection import FaceDetector
from telegram_bot import TelegramBot
from utils import (
    save_image,
    draw_status
)


class SmartSurveillanceSystem:

    def __init__(self):

        logger.system_started()

        self.camera = Camera()

        self.motion = MotionDetector()

        self.face = FaceDetector()

        self.telegram = TelegramBot()

        self.last_alert_time = 0

        self.alert_interval = 10

    def process_frame(self, frame):

        motion_found, frame, motion_count = self.motion.detect(frame)

        if motion_found:

            draw_status(frame, "Motion Detected")

            frame, faces = self.face.detect(frame)

            if len(faces) > 0:

                current_time = time.time()

                if current_time - self.last_alert_time >= self.alert_interval:

                    image_path = save_image(frame)

                    logger.image_saved(image_path)

                    self.telegram.send_alert(image_path)

                    self.last_alert_time = current_time

        else:

            draw_status(frame, "Monitoring...")

        return frame

    def run(self):

        while True:

            success, frame = self.camera.read()

            if not success:

                continue

            frame = self.process_frame(frame)

            self.camera.show(frame)

            key = self.camera.key_pressed()

            if key == ord("q"):

                break

        self.shutdown()

    def shutdown(self):

        self.camera.release()

        logger.system_stopped()


if __name__ == "__main__":

    try:

        system = SmartSurveillanceSystem()

        system.run()

    except KeyboardInterrupt:

        logger.warning("Program interrupted by user.")

    except Exception as error:

        logger.application_error(error)
