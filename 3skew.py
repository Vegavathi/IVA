import numpy as np
from skimage import io
from skimage.color  import rgb2gray
from skimage.transform import rotate
from deskew import determine_skew 

image=io.imread(r"C:\Users\vegu2\Desktop\New folder (3)\pic1.jpg")
grayscale=rgb2gray(image)
angle=determine_skew(grayscale)
rotated=rotate(image,angle,resize=True)*255
io.imsave('image1.jpg',rotated.astype(np.uint8))
