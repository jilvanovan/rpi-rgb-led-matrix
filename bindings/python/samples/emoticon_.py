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
options.brightness=100
options.multiplexing=11
options.pixel_mapper_config="V-mapper;Rotate:90"
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.gpio_slowdown=5
options.led_rgb_sequence="BGR"
options.show_refresh_rate=True
# options.limit_refresh_rate_hz=100
matrix = RGBMatrix(options = options)

print("start")

# Then scroll image across matrix...
# for n in range(-32, 33):  # Start off top-left, move off bottom-right

def emot(input,input_warna):
    out = Image.new("RGB", (64, 48), (0, 0, 0))
    # get a font
    fnt = ImageFont.truetype("emoticons.ttf", 36)
    # get a drawing context
    d = ImageDraw.Draw(out)

    if input_warna=="R":
        d.multiline_text((17, 4), input, font=fnt, fill=(255, 0, 0))
    if input_warna=="G":
        d.multiline_text((17, 4), input, font=fnt, fill=(0, 255, 0))
    if input_warna=="B":
        d.multiline_text((17, 4), input, font=fnt, fill=(0, 0, 255))        

    out.save("text.png")
    tmp=Image.new("RGB",(96,32),(0,0,0))
    data=[]
    tmpf=Image.new("RGB",(96,32),(0,0,0))

    for b in range(0,31): #sumbu x
        for v in range(0,47): # sumbu y
            coordinate = x,y = b,v
            coordinate2= x,y = v,b-6
            col=out.getpixel(coordinate) #get pixel from the current picture
            data.append(col)
            tmp.putpixel(coordinate2,col) #draw pixel from input picture
  
    tmp3=ImageOps.flip(tmp)
    tmp3.save("tmp3.png")

    for b in range(32,63): #sumbu x
        for v in range(0,47): # sumbu y
            coordinate = x,y = b,v
            coordinate2= x,y = v,b-32
            col=out.getpixel(coordinate) #get pixel from the current picture
            tmp.putpixel(coordinate2,col) #draw pixel from input picture
  
    for b in range(0,31):
        for v in range (0,47):
            coordinate3 = x,y = v,b
            coordinate4= x,y = v,b-7
            col=tmp3.getpixel(coordinate3) #get pixel from the current picture
            tmpf.putpixel(coordinate4,col) #draw pixel from input picture

    tmp.save("tmp.png")
    tmp2=ImageOps.mirror(tmp)

    for b in range(0,31):
        for v in range (47,96):
            coordinate3 = x,y = v,b
            coordinate4= x,y = v,b
            col=tmp2.getpixel(coordinate3) #get pixel from the current picture
            # print (out.getpixel(coordinate)) #print pixel from the current picture
            # data.append(col)
            tmpf.putpixel(coordinate4,col) #draw pixel from input picture

    tmp2.save("tmp2.png")
    tmpf.save("tmpf.png")
    return tmpf

def emot2():
    # out = Image.new("RGB", (64, 48), (0, 0, 0))
    # # # get a font
    # fnt = ImageFont.truetype("emoticons.ttf", 36)
    # # # get a drawing context
    # d = ImageDraw.Draw(out)

    # # if input_warna=="R":
    # d.multiline_text((17, 4), "a", font=fnt, fill=(255, 0, 0))
    # if input_warna=="G":
        # d.multiline_text((17, 4), input, font=fnt, fill=(0, 255, 0))
    # if input_warna=="B":
        # d.multiline_text((17, 4), input, font=fnt, fill=(0, 0, 255))        

    out = Image.open("marah.jpg").convert('RGB')
    print("<><><><><><><><><><><><><><><><><><><",out.width)
    print("<><><><><><><><><><><><><><><><><><><",out.height)

    out.save("text.png")
    tmp=Image.new("RGB",(96,32),(0,0,0))
    data=[]
    tmpf=Image.new("RGB",(96,32),(0,0,0))

    for b in range(0,31): #sumbu x
        for v in range(0,47): # sumbu y
            coordinate = x,y = b,v
            coordinate2= x,y = v,b-6
            col=out.getpixel(coordinate) #get pixel from the current picture
            data.append(col)
            tmp.putpixel(coordinate2,col) #draw pixel from input picture
  
    tmp3=ImageOps.flip(tmp)
    tmp3.save("tmp3.png")

    for b in range(32,63): #sumbu x
        for v in range(0,47): # sumbu y
            coordinate = x,y = b,v
            coordinate2= x,y = v,b-32
            col=out.getpixel(coordinate) #get pixel from the current picture
            tmp.putpixel(coordinate2,col) #draw pixel from input picture
  
    for b in range(0,31):
        for v in range (0,47):
            coordinate3 = x,y = v,b
            coordinate4= x,y = v,b-7
            col=tmp3.getpixel(coordinate3) #get pixel from the current picture
            tmpf.putpixel(coordinate4,col) #draw pixel from input picture

    tmp.save("tmp.png")
    tmp2=ImageOps.mirror(tmp)

    for b in range(0,31):
        for v in range (47,96):
            coordinate3 = x,y = v,b
            coordinate4= x,y = v,b
            col=tmp2.getpixel(coordinate3) #get pixel from the current picture
            # print (out.getpixel(coordinate)) #print pixel from the current picture
            # data.append(col)
            tmpf.putpixel(coordinate4,col) #draw pixel from input picture

    tmp2.save("tmp2.png")
    tmpf.save("tmpf.png")
    return tmpf


while True:

        tmpout=Image.new("RGB",(96,32),(0,0,0))
        #senyum hijau m kecil
        #senyum biru A besar
        #marah merah (
        # tmpout=emot2()
        tmpout=Image.open("paku.png").convert('RGB')
        matrix.Clear()
        matrix.SetImage(tmpout, 0, 0)           
        time.sleep(2)

# matrix.Clear()
