import cv2
img=cv2.imread(r"C:\Users\vegu2\Desktop\New folder (3)\pic1.jpg")
print('Orginal Dimensions:',img.shape)
scale_percent=40
width=int(img.shape[1]*scale_percent/100)
height=int(img.shape[0]*scale_percent/100)
dim=(width,height)

resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print('Resized Dimensions:',resized.shape)
cv2.imshow("Resized image",resized)
cv2.waitKey(0)
cv2.destoryAllWindows()
