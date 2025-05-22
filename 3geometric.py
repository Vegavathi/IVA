from PIL import Image
Orginal_image=Image.open(r"C:\Users\vegu2\Desktop\New folder (3)\pic1.jpg")
rotated_image1=Orginal_image.rotate(180)
rotated_image2=Orginal_image.transpose(Image.ROTATE_90)
rotated_image3=Orginal_image.rotate(60)
rotated_image1.show()
rotated_image2.show()
rotated_image3.show()