"""
---------------------------------------------------
Smart Surveillance System
Configuration File
---------------------------------------------------
This file contains all project settings.
Changing values here updates the whole project.
---------------------------------------------------
"""

# ==============================
# Camera Settings
# ==============================

# Default camera index
CAMERA_INDEX = 0

# Camera resolution
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Frames captured per second
FPS = 30


# ==============================
# Motion Detection Settings
# ==============================

# Ignore very small moving objects
MIN_CONTOUR_AREA = 2000

# Motion sensitivity
THRESHOLD_VALUE = 25


# ==============================
# Face Detection
# ==============================

# Haar Cascade model path
FACE_MODEL = "models/haarcascade_frontalface_default.xml"


# ==============================
# Image Storage
# ==============================

# Folder where images will be saved
IMAGE_FOLDER = "images"


# ==============================
# Telegram Bot Details
# ==============================

# Replace these with your own credentials
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"


# ==============================
# Alert Message
# ==============================

ALERT_MESSAGE = "⚠ Motion detected! Please check the attached image."
