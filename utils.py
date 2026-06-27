"""
=========================================================
utils.py

Utility functions used throughout the project.
=========================================================
"""

import os
import cv2
from datetime import datetime
import config


def get_timestamp():
    """
    Returns current date and time.
    Example:
    20250714_184530
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def get_display_time():
    """
    Returns readable timestamp.
    Example:
    14-07-2025 18:45:30
    """
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def create_image_name():

    filename = (
        config.IMAGE_PREFIX
        + "_"
        + get_timestamp()
        + config.IMAGE_EXTENSION
    )

    return filename


def get_image_path():

    filename = create_image_name()

    return os.path.join(
        config.IMAGE_FOLDER,
        filename
    )


def save_image(frame):

    path = get_image_path()

    cv2.imwrite(
        path,
        frame,
        [
            cv2.IMWRITE_JPEG_QUALITY,
            config.JPEG_QUALITY
        ]
    )

    return path


def draw_text(
    frame,
    text,
    position,
    color=config.GREEN
):

    cv2.putText(
        frame,
        text,
        position,
        config.FONT,
        config.FONT_SCALE,
        color,
        config.THICKNESS
    )


def draw_timestamp(frame):

    if config.SHOW_TIMESTAMP:

        draw_text(
            frame,
            get_display_time(),
            (10, 25),
            config.YELLOW
        )


def draw_status(frame, status):

    if config.SHOW_STATUS:

        draw_text(
            frame,
            status,
            (10, 55),
            config.GREEN
        )


def draw_fps(frame, fps):

    if config.SHOW_FPS:

        draw_text(
            frame,
            f"FPS : {int(fps)}",
            (10, 85),
            config.BLUE
        )


def file_exists(path):

    return os.path.exists(path)


def create_folder(path):

    if not os.path.exists(path):
        os.makedirs(path)


def resize_frame(frame):

    return cv2.resize(
        frame,
        (
            config.FRAME_WIDTH,
            config.FRAME_HEIGHT
        )
    )


def convert_to_gray(frame):

    return cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


def blur_image(gray):

    return cv2.GaussianBlur(
        gray,
        config.GAUSSIAN_KERNEL,
        0
    )
