import math
#import pyautogui
import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities

webcam = cv2.VideoCapture(0)

my_hands = mp.solutions.hands.Hands()
drawing_utils =mp.solutions.drawing_utils

devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume

while True:
    _,img = webcam.read()
    x1=y1=x2=y2 = 0
    frame_height,frame_width, _ = img.shape
    rgb_image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    output = my_hands.process(rgb_image) 
    hands =  output.multi_hand_landmarks
    
    if hands:
        for hand in hands:
        
            drawing_utils.draw_landmarks(img,hand)
            landmarks = hand.landmark
        
            for id,landmark  in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
        
                if id ==8 :
                    cv2.circle(img,center=(x,y),radius=8,color=(0,255,255),thickness=3)
                    x1 = x
                    y1 = y
                if id ==4:
                    cv2.circle(img,center=(x,y),radius=8,color=(255,0,255),thickness=3)
                    x2 = x
                    y2 = y


            distance = math.hypot(x2-x1, y2-y1)
            volume_percentage = np.interp(distance, [30, 250], [0, 100])
            #if distance > 50:

              #  pyautogui.press('volumeup") 
            #else:
             #   pyautogui.press("volumedown")
            volume.SetMasterVolumeLevelScalar(volume_percentage / 100,None)
            current_volume = volume.GetMasterVolumeLevelScalar() * 100
            cv2.putText(img, f'Volume: {int(current_volume)}%',
            (50, 200),
            cv2.FONT_HERSHEY_PLAIN,
            2, (255, 0, 0), 2)
            cv2.line(img,(x1,y1),(x2,y2),color=(0,255,0),thickness=3)


    cv2.imshow('Hand Gesture Volume Control', img)
    key =cv2.waitKey(10)
    if key == 27:
        break


webcam.release()
cv2.destroyAllWindows()