# Combining 2 images together

from PIL import Image

img1 = Image.open("226.jpg")
img2 = Image.open("1234.jpeg")

area = (100, 100, 625, 450)         # We have to give a calculated area of the second image to be pasted on the first, otherwise error occurs
img1.paste(img2, area)          #it takes 2 parameters. Here we are pasting img2 on img1, with the given area where the img2 will be pasted

img1.show()
