import pandas as pd
import numpy as np
import cv2

path = r'http://10.3.141.83:2020/video'
cap = cv2.VideoCapture(path)

if not cap.isOpened():
    print("Error opening the file")

while cap.isOpened():
    ret, dam = cap.read()
    
    if ret:
        resize = cv2.resize(dam, (1200, 800))
        cv2.imshow('frame', resize)
        
        if cv2.waitKey(24) & 0xFF == ord('q'):
            break
    else:
        break

