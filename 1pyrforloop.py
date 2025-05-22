import cv2
import numpy as np
img=cv2.imread(r"C:\Users\vegu2\Desktop\New folder (3)\pic1.jpg")
layer =img.copy()
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer) 
    gp.append(layer)
    cv2.imshow(str(i),layer)
cv2.imshow("orginal image",img)
cv2.waitKey(0)