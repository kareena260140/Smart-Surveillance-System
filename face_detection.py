"""
face_detection.py
Detects human faces using Haar Cascade Classifier.
"""

import cv2
import config


class FaceDetector:

    def __init__(self):

        self.face_detector = cv2.CascadeClassifier(config.FACE_MODEL)

        if self.face_detector.empty():
            raise Exception("Unable to load Haar Cascade model.")

    def detect_faces(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_detector.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

        return frame, faces
