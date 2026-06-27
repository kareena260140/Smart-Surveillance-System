"""
=========================================================
Smart Surveillance System
Configuration File
=========================================================

Author : Kareena
Language : Python 3.10+
Framework : OpenCV

=========================================================
"""

import os

# =========================================================
# PROJECT INFORMATION
# =========================================================

PROJECT_NAME = "Smart Surveillance System"

VERSION = "2.0"

AUTHOR = "Kareena"

# =========================================================
# DIRECTORY SETTINGS
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGE_FOLDER = os.path.join(BASE_DIR, "images")

LOG_FOLDER = os.path.join(BASE_DIR, "logs")

MODEL_FOLDER = os.path.join(BASE_DIR, "models")

# Automatically create required folders

os.makedirs(IMAGE_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)
os.makedirs(MODEL_FOLDER, exist_ok=True)

# =========================================================
# CAMERA SETTINGS
# =========================================================

CAMERA_INDEX = 0

FRAME_WIDTH = 640

FRAME_HEIGHT = 480

FPS = 30

WINDOW_NAME = "Smart Surveillance System"

# =========================================================
# MOTION DETECTION SETTINGS
# =========================================================

MIN_CONTOUR_AREA = 2500

THRESHOLD_VALUE = 25

GAUSSIAN_KERNEL = (21, 21)

DILATION_ITERATIONS = 2

# =========================================================
# FACE DETECTION SETTINGS
# =========================================================

FACE_MODEL = os.path.join(
    MODEL_FOLDER,
    "haarcascade_frontalface_default.xml"
)

FACE_SCALE_FACTOR = 1.2

FACE_MIN_NEIGHBORS = 5

FACE_MIN_SIZE = (30, 30)

# =========================================================
# IMAGE SETTINGS
# =========================================================

IMAGE_PREFIX = "intruder"

IMAGE_EXTENSION = ".jpg"

JPEG_QUALITY = 95

# =========================================================
# TELEGRAM SETTINGS
# =========================================================

BOT_TOKEN = "YOUR_BOT_TOKEN"

CHAT_ID = "YOUR_CHAT_ID"

ALERT_MESSAGE = """
⚠ Smart Surveillance Alert

Motion Detected!

Face Detected!

Please check the attached image.
"""

# =========================================================
# LOGGING
# =========================================================

LOG_FILE = os.path.join(
    LOG_FOLDER,
    "system.log"
)

# =========================================================
# DISPLAY SETTINGS
# =========================================================

SHOW_FPS = True

SHOW_RECTANGLES = True

SHOW_TIMESTAMP = True

SHOW_STATUS = True

# =========================================================
# COLORS (BGR FORMAT)
# =========================================================

GREEN = (0,255,0)

RED = (0,0,255)

BLUE = (255,0,0)

WHITE = (255,255,255)

BLACK = (0,0,0)

YELLOW = (0,255,255)

# =========================================================
# FONT SETTINGS
# =========================================================

FONT = 0

FONT_SCALE = 0.7

THICKNESS = 2
