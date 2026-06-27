"""
camera.py
Handles camera initialization and frame capture.
"""

import cv2
import config


class Camera:

    def __init__(self):
        self.camera = cv2.VideoCapture(config.CAMERA_INDEX)

        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, config.FRAME_WIDTH)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, config.FRAME_HEIGHT)
        self.camera.set(cv2.CAP_PROP_FPS, config.FPS)

        if not self.camera.isOpened():
            raise Exception("Unable to access camera.")

    def get_frame(self):
        success, frame = self.camera.read()

        if not success:
            return None

        return frame

    def release(self):
        self.camera.release()


if __name__ == "__main__":

    cam = Camera()

    while True:

        frame = cam.get_frame()

        if frame is None:
            break

        cv2.imshow("Smart Surveillance Camera", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
