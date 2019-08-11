# Giving Filters to images
# Individual Channels

from PIL import Image

img = Image.open("226.jpg")
print(img.mode)         # RGB is the mode

r, g, b = img.split()       # It returns a tuple of 3 images i.e, the amount of red, green and blue in the image

r.show()
g.show()
b.show()

# Merging effect -> merging the individual channels of R,G,B to create a filter

img1 = Image.merge("RGB", (r, g, b))        # It takes in the mode and the colours
# In the above case, it will print the same image

img2 = Image.merge("RGB", (b, g, r))
img2.show()

img3 = Image.merge("RGB", (g, r, b))
img3.show()

img4 = Image.merge("RGB", (b, g, b))
img4.show()

# It just takes in the amount of R,G,B in the given given format(RGB), but different permutations give different results
# Likewise we can use any other permutations, to form different filters of the images

# Double Exposure:
# to use this, the two images must be of the same size

new_img1 = Image.open("1_Earth.jpg")
new_img2 = Image.open("1_mario.jpg")

r1, b1, g1 = new_img1.split()
r2, b2, g2 = new_img2.split()

final_image = Image.merge("RGB", (r1, b2, g1))
final_image.show()