# Modes and Filters

from PIL import Image
from PIL import ImageFilter              # Contains pretty cool built in filters
img = Image.open("226.jpg")

#Converting to black and white

black_white = img.convert("L")           # It takes in the format of the image you want to convert into. Eg: RGB, CMYK, L
# L -> Luminance, which basically means black and white
# CMYK -> Cyan, Magenta, Yellow, Key(Black), which is generally used in colour printing, pretty much same as RGB

black_white.show()

cmyk_img = img.convert("CMYK")
cmyk_img.show()

# Using image filters

blur_img = img.filter(ImageFilter.BLUR)
blur_img.show()

detail_img = img.filter(ImageFilter.DETAIL)
detail_img.show()

edges_img = img.filter(ImageFilter.FIND_EDGES)
edges_img.show()