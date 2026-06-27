"""
main.py
Main program for Smart Surveillance System
"""

import os
import cv2
from datetime import datetime

import config
from camera import Camera
from motion import MotionDetector
from face_detection import FaceDetector
from telegram_bot import TelegramBot


def create_folder():

    if not os.path.exists(config.IMAGE_FOLDER):
        os.makedirs(config.IMAGE_FOLDER)


def save_image(frame):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = os.path.join(
        config.IMAGE_FOLDER,
        f"intruder_{timestamp}.jpg"
    )

    cv2.imwrite(filename, frame)

    return filename


def main():

    create_folder()

    camera = Camera()

    motion_detector = MotionDetector()

    face_detector = FaceDetector()

    telegram = TelegramBot()

    print("Smart Surveillance System Started...")
    print("Press 'Q' to Exit.")

    while True:

        frame = camera.get_frame()

        if frame is None:
            break

        motion_detected, motion_frame = motion_detector.detect_motion(frame)

        display_frame = motion_frame

        if motion_detected:

            display_frame, faces = face_detector.detect_faces(display_frame)

            if len(faces) > 0:

                image_path = save_image(display_frame)

                telegram.send_message(config.ALERT_MESSAGE)

                telegram.send_photo(image_path)

                cv2.putText(
                    display_frame,
                    "ALERT SENT",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

        cv2.imshow("Smart Surveillance System", display_frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    camera.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
