#!/usr/bin/env python

# (This is an example similar to an example from the Adafruit fork
#  to show the similarities. Most important difference currently is, that
#  this library wants RGB mode.)
#
# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

from PIL import Image
from PIL import ImageDraw
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont,ImageOps
import numpy as np

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 16
options.cols = 32
options.chain_length = 6
options.parallel = 1
options.brightness=10
options.multiplexing=11
options.pixel_mapper_config="V-mapper;Rotate:90"
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.gpio_slowdown=5
matrix = RGBMatrix(options = options)


# Then scroll image across matrix...
# for n in range(-32, 33):  # Start off top-left, move off bottom-right

out = Image.new("RGB", (64, 48), (0, 0, 0))

# get a font
fnt = ImageFont.truetype("arial.ttf", 36)
# get a drawing context
d = ImageDraw.Draw(out)

# draw multiline text
d.multiline_text((12, 4), "65", font=fnt, fill=(0, 255, 0))
# 
# out.getpixel()


# coordinate = x, y = 10, 10
# print (out.getpixel(coordinate))
print("start")
# print(out.getpixel())
out.save("text.png")

tmp=Image.new("RGB",(96,32),(0,0,0))
data=[]

for b in range(0,31): #sumbu x
    for v in range(0,41): # sumbu y
        coordinate = x,y = b,v
        coordinate2= x,y = v,b-10
        col=out.getpixel(coordinate) #get pixel from the current picture
        print (out.getpixel(coordinate)) #print pixel from the current picture
        data.append(col)
        tmp.putpixel(coordinate2,col) #draw pixel from input picture
print(data)

for b in range(32,60): #sumbu x
    for v in range(0,41): # sumbu y
        coordinate = x,y = b,v
        coordinate2= x,y = v+50,b-30
        col=out.getpixel(coordinate) #get pixel from the current picture
        print (out.getpixel(coordinate)) #print pixel from the current picture
        data.append(col)
        tmp.putpixel(coordinate2,col) #draw pixel from input picture
print(data)

# for b in range(31,32): #sumbu x
#     for v in range(0,47): # sumbu y
#         coordinate = x,y = v,b
#         coordinate2= x,y = b-10,v-17
#         col=out.getpixel(coordinate) #get pixel from the current picture
#         print (out.getpixel(coordinate)) #print pixel from the current picture
#         tmp.putpixel(coordinate2,col) #draw pixel from input picture


tmp.save("tmp.png")
tmp2=ImageOps.flip(tmp)
tmp2.save("tmp2.png")
# tmp=Image.new("RGB",(96,32),(0,0,0))
# for 

matrix.Clear()
matrix.SetImage(tmp, 0, 0)
# time.sleep(10)

# matrix.Clear()
