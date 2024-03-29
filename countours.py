# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 21:24:49 2024

@author: HP
"""

import cv2
import numpy as np
original_image=cv2.imread("C:/Users/HP/Desktop/images/opencv.png")
image=cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
RET,image = cv2.threshold(image, 170, 225,0)

#image= cv2.Canny(image,30,70)

contours,hierarchy=cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(original_image, contours, -1, (200,100,0),5)
print(len(contours))

cv2.imshow("original image",original_image)
cv2.waitKey()
cv2.destroyAllWindows()