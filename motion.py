"""
motion.py
Detects motion by comparing consecutive video frames.
"""

import cv2
import config


class MotionDetector:

    def __init__(self):
        self.previous_frame = None

    def detect_motion(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.previous_frame is None:
            self.previous_frame = gray
            return False, frame

        frame_difference = cv2.absdiff(self.previous_frame, gray)

        threshold = cv2.threshold(
            frame_difference,
            config.THRESHOLD_VALUE,
            255,
            cv2.THRESH_BINARY
        )[1]

        threshold = cv2.dilate(threshold, None, iterations=2)

        contours, _ = cv2.findContours(
            threshold,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        motion_found = False

        for contour in contours:

            if cv2.contourArea(contour) < config.MIN_CONTOUR_AREA:
                continue

            motion_found = True

            (x, y, w, h) = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        self.previous_frame = gray

        return motion_found, frame
