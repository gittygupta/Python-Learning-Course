# Cropping

from PIL import Image

img = Image.open("226.jpg")
area = (100, 100, 400, 400)         # The 1st 2 numbers are x,y coordinates of the top left corner and the last 2 are of the bottom right corner
# area is a 4 value tuple
cropped_img = img.crop(area)        # The only parameter it takes is a 4 value tuple

img.show()
cropped_img.show()