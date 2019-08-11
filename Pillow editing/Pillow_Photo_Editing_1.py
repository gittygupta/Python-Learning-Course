# Introduction

from PIL import Image

img = Image.open("226.jpg")
print(img.size)
print(img.format)

img.show()      #as the console cant open images, so it opens the photos app to show the image

