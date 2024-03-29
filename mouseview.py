# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:50:00 2024

@author: HP
"""

import cv2
import numpy as np


image1= cv2.imread("C:/Users/HP/Desktop/images/lena.jpg")
row,col,ch = image1.shape

x = 0
y = 0
while (True):
    
    T = np.float64([[1,0,x],[1,0,y]])
    image2=cv2.warpAffine(image1, T, (col,row))
    
    cv2.imshow("Frame1", image1)
    cv2.imshow("Frame2", image2)
    
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
    x=x+.1
    
cv2.destroyAllWindows()