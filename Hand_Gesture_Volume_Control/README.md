# Hand Gesture Volume Control using Python

## Overview

A real-time hand gesture volume control application using Python,
OpenCV, and MediaPipe. It captures video from a webcam, tracks the thumb
and index fingertip, calculates the distance between them, and uses that
distance to control the Windows master volume.

## Technologies

-   Python
-   OpenCV
-   MediaPipe
-   NumPy
-   Pycaw

## How it works

1.  Capture live video from the webcam.
2.  Detect hand landmarks using MediaPipe.
3.  Track the thumb tip (landmark 4) and index fingertip (landmark 8).
4.  Calculate the distance between the two fingertips.
5.  Map the distance to a volume percentage.
6.  Adjust the Windows master volume using Pycaw.
7.  Display the hand landmarks, fingertip distance, and volume level.

## How to run

Install the required libraries:

``` bash
pip install opencv-python mediapipe==0.10.21 numpy pycaw comtypes
```

Run:

``` bash
python app.py
```

Move your thumb and index finger apart to increase the volume, and bring
them closer to decrease it.

Press `ESC` to exit.

## Learning outcomes

-   Webcam access using OpenCV
-   Hand landmark detection using MediaPipe
-   Tracking specific hand landmarks
-   Calculating distance between two points
-   Mapping distance values to a percentage
-   Controlling Windows master volume using Pycaw
-   Real-time video processing
