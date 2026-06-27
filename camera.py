"""
=========================================================
camera.py

Camera Module
Initializes camera, captures frames and calculates FPS.
=========================================================
"""

import time
import cv2

import config
from logger import logger
from utils import (
    resize_frame,
    draw_timestamp,
    draw_fps
)


class Camera:

    def __init__(self):

        self.camera = None

        self.frame = None

        self.start_time = time.time()

        self.frame_count = 0

        self.fps = 0

        self.initialize_camera()

    def initialize_camera(self):

        self.camera = cv2.VideoCapture(config.CAMERA_INDEX)

        self.camera.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            config.FRAME_WIDTH
        )

        self.camera.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            config.FRAME_HEIGHT
        )

        self.camera.set(
            cv2.CAP_PROP_FPS,
            config.FPS
        )

        if not self.camera.isOpened():

            logger.camera_failed()

            raise Exception(
                "Unable to access camera."
            )

        logger.camera_connected()

    def calculate_fps(self):

        self.frame_count += 1

        elapsed = time.time() - self.start_time

        if elapsed >= 1:

            self.fps = self.frame_count / elapsed

            self.frame_count = 0

            self.start_time = time.time()

    def read(self):

        success, frame = self.camera.read()

        if not success:

            logger.error(
                "Unable to read camera frame."
            )

            return False, None

        frame = resize_frame(frame)

        self.calculate_fps()

        draw_timestamp(frame)

        draw_fps(frame, self.fps)

        return True, frame

    def show(self, frame):

        cv2.imshow(
            config.WINDOW_NAME,
            frame
        )

    def key_pressed(self):

        key = cv2.waitKey(1) & 0xFF

        return key

    def release(self):

        if self.camera is not None:

            self.camera.release()

        cv2.destroyAllWindows()

        logger.system_stopped()

    def reconnect(self):

        logger.warning(
            "Reconnecting camera..."
        )

        self.release()

        time.sleep(2)

        self.initialize_camera()

    def get_fps(self):

        return self.fps


if __name__ == "__main__":

    logger.system_started()

    camera = Camera()

    while True:

        success, frame = camera.read()

        if not success:

            camera.reconnect()

            continue

        camera.show(frame)

        if camera.key_pressed() == ord("q"):

            break

    camera.release()
