#Basic transformations

from PIL import Image

img = Image.open("226.jpg")

# Squarring the image -> just compresses the image size without cropping it

square_img = img.resize((400, 400))       # Takes in a tuple
square_img.show()

# For any kind of rotation or flipping of image, always use "transpose" function

# Flip

flip_img1 = img.transpose(Image.FLIP_LEFT_RIGHT)
flip_img2 = img.transpose(Image.FLIP_TOP_BOTTOM)
flip_img1.show()
flip_img2.show()

# Rotate

spin_img1 = img.transpose(Image.ROTATE_90)
spin_img2 = img.transpose(Image.ROTATE_180)
spin_img3 = img.transpose(Image.ROTATE_270)

spin_img1.show()
spin_img2.show()
spin_img3.show()