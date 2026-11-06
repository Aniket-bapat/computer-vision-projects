# Real-Time Face Detection using OpenCV

## Overview
A simple real-time face detection application using Python and OpenCV. It captures video from a webcam, detects frontal faces using a Haar Cascade classifier, and draws bounding boxes around detected faces.

## Technologies
- Python
- OpenCV
- Haar Cascade Classifier

## How it works
1. Capture live video from the webcam.
2. Convert each frame into grayscale.
3. Detect faces using Haar Cascade.
4. Draw bounding boxes around detected faces.
5. Display the processed video.

## How to run

Install OpenCV:

```bash
pip install opencv-contrib-python
```

Run:

```bash
python app.py
```

Press `ESC` to exit.

## Learning outcomes
- Webcam access using OpenCV
- Image colour-space conversion
- Haar Cascade face detection
- Bounding box visualisation
- Real-time video processing