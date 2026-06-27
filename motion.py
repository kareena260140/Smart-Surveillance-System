"""
=========================================================
motion.py

Motion Detection Module
=========================================================
"""

import cv2
import config
from logger import logger


class MotionDetector:

    def __init__(self):

        self.previous_frame = None

        self.motion_counter = 0

        self.motion_detected = False

    def preprocess(self, frame):

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        gray = cv2.GaussianBlur(
            gray,
            config.GAUSSIAN_KERNEL,
            0
        )

        return gray

    def find_difference(
        self,
        previous,
        current
    ):

        difference = cv2.absdiff(
            previous,
            current
        )

        return difference

    def threshold_image(self, difference):

        threshold = cv2.threshold(
            difference,
            config.THRESHOLD_VALUE,
            255,
            cv2.THRESH_BINARY
        )[1]

        threshold = cv2.dilate(
            threshold,
            None,
            iterations=config.DILATION_ITERATIONS
        )

        return threshold

    def find_contours(self, threshold):

        contours, _ = cv2.findContours(
            threshold,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        return contours

    def draw_contours(
        self,
        frame,
        contours
    ):

        detected = False

        count = 0

        total_area = 0

        for contour in contours:

            area = cv2.contourArea(contour)

            if area < config.MIN_CONTOUR_AREA:
                continue

            detected = True

            count += 1

            total_area += area

            x, y, w, h = cv2.boundingRect(contour)

            if config.SHOW_RECTANGLES:

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    config.GREEN,
                    2
                )

                cv2.putText(
                    frame,
                    "Motion",
                    (x, y - 8),
                    config.FONT,
                    0.5,
                    config.GREEN,
                    2
                )

        return detected, count, total_area

    def detect(self, frame):

        gray = self.preprocess(frame)

        if self.previous_frame is None:

            self.previous_frame = gray

            return False, frame, 0

        difference = self.find_difference(
            self.previous_frame,
            gray
        )

        threshold = self.threshold_image(
            difference
        )

        contours = self.find_contours(
            threshold
        )

        detected, count, total_area = self.draw_contours(
            frame,
            contours
        )

        if detected:

            self.motion_counter += 1

            self.motion_detected = True

            logger.motion_detected()

            cv2.putText(
                frame,
                "MOTION DETECTED",
                (10, 120),
                config.FONT,
                0.7,
                config.RED,
                2
            )

        else:

            self.motion_detected = False

            cv2.putText(
                frame,
                "NO MOTION",
                (10, 120),
                config.FONT,
                0.7,
                config.GREEN,
                2
            )

        self.previous_frame = gray

        return detected, frame, count

    def get_motion_count(self):

        return self.motion_counter

    def reset_counter(self):

        self.motion_counter = 0

    def is_motion_detected(self):

        return self.motion_detected
