# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 22:11:21 2024

@author: HP
"""

import cv2
import numpy as np

kernal= np.ones((512,512,3),np.uint8)
kernal=kernal*255

cv2.rectangle(kernal, (50,50), (150,150),(0,0,0),-1)

cv2.circle(kernal, (100,250),90,(0,0,0),-1)
cv2.ellipse(kernal, (350,300), (150,200),0,0,360,(0,0,0),-1)

cv2.imwrite("shapes.jpg",kernal)
cv2.imshow("image",kernal)
cv2.waitKey()
cv2.destroyAllWindows()