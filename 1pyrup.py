# upscale
import cv2
import numpy as np
img=cv2.imread(r"C:\Users\vegu2\Desktop\New folder (3)\pic1.jpg")
ir1=cv2.pyrDown(img)
ir2=cv2.pyrDown(ir1)
hr=cv2.pyrUp(ir2)
cv2.imshow("original image",img)
cv2.imshow("pyrDown 1 image",ir1)
cv2.imshow("pyrDown 2 image",ir2)
cv2.imshow("pyrup image",hr)
cv2.waitKey(0)