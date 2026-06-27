# Smart Surveillance System using Raspberry Pi and OpenCV

A Raspberry Pi based Smart Surveillance System that performs real-time motion detection and face detection using OpenCV. Whenever motion is detected, the system captures an image, detects faces, stores the image locally, and sends an alert to the user's Telegram account.

---

## Features

- Real-time video monitoring
- Motion Detection
- Face Detection using Haar Cascade
- Telegram Notification
- Automatic Image Capture
- Timestamped Image Storage
- Modular Python Code

---

## Hardware Used

- Raspberry Pi 4 Model B
- Raspberry Pi Camera Module V2
- 32GB Micro SD Card
- 5V 3A USB-C Adapter
- Wi-Fi Router

---

## Software Used

- Raspberry Pi OS
- Python 3
- OpenCV
- NumPy
- Requests
- Telegram Bot API

---

## Folder Structure

```
Smart-Surveillance-System/

config.py

camera.py

motion.py

face_detection.py

telegram_bot.py

main.py

models/

images/

logs/
```

---

## Workflow

Camera

↓

Capture Frame

↓

Motion Detection

↓

Face Detection

↓

Save Image

↓

Telegram Alert

---

## Future Improvements

- Face Recognition
- Email Alerts
- Cloud Storage
- Video Recording
- Firebase Integration
- Intruder Database

---

## Author

Kareena
