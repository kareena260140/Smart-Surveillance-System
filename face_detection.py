"""
=========================================================
face_detection.py

Face Detection Module
=========================================================
"""

import cv2
import config
from logger import logger


class FaceDetector:

    def __init__(self):

        self.face_model = cv2.CascadeClassifier(
            config.FACE_MODEL
        )

        if self.face_model.empty():

            logger.model_failed()

            raise Exception(
                "Unable to load Haar Cascade Model."
            )

        logger.model_loaded()

        self.total_faces = 0

    def detect(self, frame):

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        faces = self.face_model.detectMultiScale(
            gray,
            scaleFactor=config.FACE_SCALE_FACTOR,
            minNeighbors=config.FACE_MIN_NEIGHBORS,
            minSize=config.FACE_MIN_SIZE
        )

        face_count = len(faces)

        if face_count > 0:

            self.total_faces += face_count

            logger.face_detected(face_count)

        for (x, y, w, h) in faces:

            if config.SHOW_RECTANGLES:

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    config.BLUE,
                    2
                )

                cv2.putText(
                    frame,
                    "Face",
                    (x, y - 10),
                    config.FONT,
                    0.6,
                    config.BLUE,
                    2
                )

        cv2.putText(
            frame,
            f"Faces : {face_count}",
            (10, 155),
            config.FONT,
            0.7,
            config.BLUE,
            2
        )

        return frame, faces

    def get_total_faces(self):

        return self.total_faces

    def reset_counter(self):

        self.total_faces = 0

    def face_available(self, faces):

        return len(faces) > 0
