import urllib.request
import random

def download_image_file(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".png"
    urllib.request.urlretrieve(url, full_name) # used to retrive url to download the image
    # it also stores the name of the file and saves the image in the same directory as the program

    # .jpg / .png is written at the end of full_name because python stores images as numbers

download_image_file("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Sunflower_from_Silesia2.jpg/800px-Sunflower_from_Silesia2.jpg")