import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(r"C:\Users\vegu2\Desktop\New folder (3)\pic1.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rows,cols,ch=img.shape

pt1=np.float32([[50,50],[200,50],[50,200]])
pt2=np.float32([[10,100],[200,50],[100,250]])
Mat=cv2.getAffineTransform(pt1,pt2)
dst=cv2.warpAffine(img,Mat,(cols,rows))
plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(img)
plt.title('Input')
plt.subplot(122)
plt.imshow(dst)
plt.title('Output')
plt.show()
