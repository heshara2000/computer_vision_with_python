# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:37:20 2024

@author: HP
"""


import cv2
image= cv2.VideoCapture(0)
fourcc_Code = cv2.VideoWriter_fourcc(*"XVID")
video = cv2.VideoWriter(("my video.avi"), fourcc_Code,20.0,(640,480))

while (True):
    check,frame = image.read()
    video.write(frame)
    cv2.imshow("my image", frame)
    if cv2.waitKey(1) ==ord("q"):
        break
    print(frame.shape)
    
    cv2.imwrite("my image.jpg", frame)
    
video.release()
image.release()
cv2.destroyAllWindows()
