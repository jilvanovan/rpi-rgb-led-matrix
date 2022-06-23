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

from itertools import count
from PIL import Image
from PIL import ImageDraw
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont,ImageOps
import numpy as np
import threading
from datetime import datetime


from serial_spd_thread import serial_main_thread

class led_main_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.spd_main = serial_main_thread()
        print("[LED] Init ..........)")
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
#        options.show_refresh_rate=True
        # options.limit_refresh_rate_hz=60
        options.led_rgb_sequence="BGR"
        self.matrix = RGBMatrix(options = options)        
        self.active = False
        time.sleep(1)
        print("[LED] Initialization completed")

    def close(self):
        self.active = False
        print("[LED] Thread closed")

    @staticmethod
    def fontdrawer(input):
        out = Image.new("RGB", (64, 48), (0, 0, 0))
        # get a font
        fnt = ImageFont.truetype("/home/pi/display16x32/rpi-rgb-led-matrix/bindings/python/samples/ab.ttf", 38)
        # get a drawing context
        d = ImageDraw.Draw(out)
        # d.multiline_text((12, 4), input, font=fnt, fill=(0, 255, 0))
        buffint = int(input)

        if buffint>0 and buffint < 20:
            d.multiline_text((12, 10), input.zfill(2), font=fnt, fill=(0, 255, 0))
        if buffint>20 and buffint < 40:
            d.multiline_text((12, 10), input.zfill(2), font=fnt, fill=(0, 255, 255))
        if buffint> 40:
            d.multiline_text((12, 10), input.zfill(2), font=fnt, fill=(0, 0, 255))     


        out.save("text.png")
        tmp=Image.new("RGB",(96,32),(0,0,0))
        data=[]
        tmpf=Image.new("RGB",(96,32),(0,0,0))
        for b in range(0,31): #sumbu x
            for v in range(0,41): # sumbu y
                coordinate = x,y = b,v
                coordinate2= x,y = v,b-10
                col=out.getpixel(coordinate) #get pixel from the current picture
                data.append(col)
                tmp.putpixel(coordinate2,col) #draw pixel from input picture
        tmp3=ImageOps.flip(tmp)
        tmp3.save("tmp3.png")

        for b in range(32,60): #sumbu x
            for v in range(0,41): # sumbu y
                coordinate = x,y = b,v
                coordinate2= x,y = v,b-30
                col=out.getpixel(coordinate) #get pixel from the current picture
                tmp.putpixel(coordinate2,col) #draw pixel from input picture

        for b in range(0,32):
            for v in range (0,48):
                coordinate3 = x,y = v,b
                coordinate4= x,y = v,b-7
                col=tmp3.getpixel(coordinate3) #get pixel from the current picture
                tmpf.putpixel(coordinate4,col) #draw pixel from input picture
        tmp.save("tmp.png")
        tmp2=ImageOps.mirror(tmp)
        for b in range(0,32):
            for v in range (48,96):
                coordinate3 = x,y = v,b
                coordinate4= x,y = v,b
                col=tmp2.getpixel(coordinate3) #get pixel from the current picture
                tmpf.putpixel(coordinate4,col) #draw pixel from input picture
        tmp2.save("tmp2.png")
        tmpf.save("tmpf.png")
        return tmpf

    @staticmethod
    def fontdrawer_single(input):
        out = Image.new("RGB", (64, 48), (0, 0, 0))
        # get a font
        fnt = ImageFont.truetype("/home/pi/display16x32/rpi-rgb-led-matrix/bindings/python/samples/ab.ttf", 50)
        # get a drawing context
        d = ImageDraw.Draw(out)
        buffint = int(input)
        if buffint>0 and buffint < 20:
            d.multiline_text((14, 5), input, font=fnt, fill=(0, 255, 0))
        if buffint>20 and buffint < 40:
            d.multiline_text((14, 5), input, font=fnt, fill=(0, 255, 255))
        if buffint> 40:
            d.multiline_text((14, 5), input, font=fnt, fill=(0, 0, 255))     

        # out.save("text.png")
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
        # tmp3.save("tmp3.png")

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

        # tmp.save("tmp.png")
        tmp2=ImageOps.mirror(tmp)

        for b in range(0,31):
            for v in range (47,96):
                coordinate3 = x,y = v,b
                coordinate4= x,y = v,b
                col=tmp2.getpixel(coordinate3) #get pixel from the current picture
                # print (out.getpixel(coordinate)) #print pixel from the current picture
                # data.append(col)
                tmpf.putpixel(coordinate4,col) #draw pixel from input picture

        # tmp2.save("tmp2.png")
        # tmpf.save("tmpf.png")
        return tmpf


    @staticmethod
    def fontdrawer_double(input):
        out = Image.new("RGB", (64, 48), (0, 0, 0))
        # get a font
        fnt = ImageFont.truetype("/home/pi/display16x32/rpi-rgb-led-matrix/bindings/python/samples/ab.ttf", 50)
        # get a drawing context
        d = ImageDraw.Draw(out)
        buffint = int(input)
        if buffint>0 and buffint < 20:
            d.multiline_text((5, 5), input, font=fnt, fill=(0, 255, 0))
        if buffint>=20 and buffint <= 50:
            d.multiline_text((5, 5), input, font=fnt, fill=(255, 215, 0))
        if buffint> 50:
            d.multiline_text((5, 5), input, font=fnt, fill=(255, 0, 0))     

        # out.save("text.png")
        tmp=Image.new("RGB",(96,32),(0,0,0))
        data=[]
        tmpf=Image.new("RGB",(96,32),(0,0,0))

        for b in range(0,31): #sumbu x
            for v in range(0,46): # sumbu y
                coordinate = x,y = b,v
                coordinate2= x,y = v,b-1
                col=out.getpixel(coordinate) #get pixel from the current picture
                data.append(col)
                tmp.putpixel(coordinate2,col) #draw pixel from input picture
    
        tmp3=ImageOps.flip(tmp)
        # tmp3.save("tmp3.png")

        for b in range(32,63): #sumbu x
            for v in range(0,47): # sumbu y
                coordinate = x,y = b,v
                coordinate2= x,y = v,b-32
                col=out.getpixel(coordinate) #get pixel from the current picture
                tmp.putpixel(coordinate2,col) #draw pixel from input picture
    
        for b in range(0,31):
            for v in range (0,47):
                coordinate3 = x,y = v,b
                coordinate4= x,y = v,b
                col=tmp3.getpixel(coordinate3) #get pixel from the current picture
                tmpf.putpixel(coordinate4,col) #draw pixel from input picture

        # tmp.save("tmp.png")
        tmp2=ImageOps.mirror(tmp)

        for b in range(0,31):
            for v in range (47,96):
                coordinate3 = x,y = v,b
                coordinate4= x,y = v,b
                col=tmp2.getpixel(coordinate3) #get pixel from the current picture
                # print (out.getpixel(coordinate)) #print pixel from the current picture
                # data.append(col)
                tmpf.putpixel(coordinate4,col) #draw pixel from input picture

        # tmp2.save("tmp2.png")
        # tmpf.save("tmpf.png")
        return tmpf

    def fontdrawer2(input):
        out = Image.new("RGB", (64, 48), (0, 0, 0))
        fnt = ImageFont.truetype("/home/pi/display16x32/rpi-rgb-led-matrix/bindings/python/samples/ab.ttf", 36)
        d = ImageDraw.Draw(out)
        d.multiline_text((2, 4), input, font=fnt, fill=(0, 0, 255))
        # out.save("text.png")
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
        # tmp3.save("tmp3.png")
        for b in range(32,63): #sumbu x
            for v in range(0,47): # sumbu y
                coordinate = x,y = b,v
                coordinate2= x,y = v,b-33
                col=out.getpixel(coordinate) #get pixel from the current picture
                tmp.putpixel(coordinate2,col) #draw pixel from input picture
        for b in range(0,31):
            for v in range (0,47):
                coordinate3 = x,y = v,b
                coordinate4= x,y = v,b-7
                col=tmp3.getpixel(coordinate3) #get pixel from the current picture
                tmpf.putpixel(coordinate4,col) #draw pixel from input picture
        # tmp.save("tmp.png")
        tmp2=ImageOps.mirror(tmp)
        for b in range(0,31):
            for v in range (47,96):
                coordinate3 = x,y = v,b
                coordinate4= x,y = v,b
                col=tmp2.getpixel(coordinate3) #get pixel from the current picture
                tmpf.putpixel(coordinate4,col) #draw pixel from input picture
        # tmp2.save("tmp2.png")
        # tmpf.save("tmpf.png")
        return tmpf

    @staticmethod
    def emot(input,input_warna):
        out = Image.new("RGB", (64, 48), (0, 0, 0))
        # get a font
        fnt = ImageFont.truetype("/home/pi/display16x32/rpi-rgb-led-matrix/bindings/python/samples/emoticons_outline.ttf", 36)
        # get a drawing context
        d = ImageDraw.Draw(out)

        if input_warna=="R":
            d.multiline_text((17, 4), input, font=fnt, fill=(0, 255, 255))
        if input_warna=="G":
            d.multiline_text((17, 4), input, font=fnt, fill=(0, 255, 0))
        if input_warna=="B":
            d.multiline_text((17, 4), input, font=fnt, fill=(0, 0, 255))        

        # out.save("text.png")
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
        # tmp3.save("tmp3.png")

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

        # tmp.save("tmp.png")
        tmp2=ImageOps.mirror(tmp)

        for b in range(0,31):
            for v in range (47,96):
                coordinate3 = x,y = v,b
                coordinate4= x,y = v,b
                col=tmp2.getpixel(coordinate3) #get pixel from the current picture
                # print (out.getpixel(coordinate)) #print pixel from the current picture
                # data.append(col)
                tmpf.putpixel(coordinate4,col) #draw pixel from input picture

        # tmp2.save("tmp2.png")
        # tmpf.save("tmpf.png")
        return tmpf

    def run(self):
        self.active = True
        print(f"[LED] Thread started")
        self.spd_main.start()
        # tmpout=Image.new("RGB",(96,32),(0,0,0))
        # tmpout=self.emot("A","R")
        # self.matrix.Clear()
        # self.matrix.SetImage(tmpout, 0, 0)           
        # time.sleep(1)
        # tmpout=self.emot("m","R")
        # self.matrix.Clear()
        # self.matrix.SetImage(tmpout, 0, 0)
        # time.sleep(1)

        while self.active:
            buff = self.spd_main.spd_buff
            buff2 = self.spd_main.emote_status
            # print("[LED Thread] Sped Value : ",buff)
            # print("[LED Thread] Emote status Value : ",buff2)
            self.matrix.Clear()
            if buff != 0:

                for counter in range (0,11):
                    print(counter)    
                    tmpout=Image.new("RGB",(96,32),(0,0,0))
                    if self.spd_main.spd_buff>buff:
                        buff=self.spd_main.spd_buff
                    if buff<10:
                        tmpout=self.fontdrawer_single(str(buff))
                        self.matrix.Clear()
                        self.matrix.SetImage(tmpout, 0, 0)
                    if buff>10:
                        tmpout=self.fontdrawer_double(str(buff))
                        self.matrix.Clear()
                        self.matrix.SetImage(tmpout, 0, 0)
                    time.sleep(0.5)

                print("[LED Thread] Sped Value : ",buff)        
                if buff >0 and buff <=20:
                    tmpout=Image.new("RGB",(96,32),(0,0,0))
                    tmpout=tmpout=Image.open("/home/pi/display16x32/rpi-rgb-led-matrix/bindings/python/samples/bagoy.png").convert('RGB')
                    self.matrix.Clear()
                    self.matrix.SetImage(tmpout, 0, 0)           
                    time.sleep(0.5)
                if buff >20 and buff <=50:
                    tmpout=Image.new("RGB",(96,32),(0,0,0))
                    # tmpout=self.emot("A","R")
                    tmpout=tmpout=Image.open("/home/pi/display16x32/rpi-rgb-led-matrix/bindings/python/samples/bagoy.png").convert('RGB')
                    self.matrix.Clear()
                    self.matrix.SetImage(tmpout, 0, 0)           
                    time.sleep(0.5)
                if buff >50 :
                    # tmpout=Image.new("RGB",(96,32),(0,0,0))
                    tmpout=tmpout=Image.open("/home/pi/display16x32/rpi-rgb-led-matrix/bindings/python/samples/marah.png").convert('RGB')
#                    tmpout=self.emot("(","B")
                    self.matrix.Clear()
                    self.matrix.SetImage(tmpout, 0, 0)           
                    time.sleep(0.75)
            if self.spd_main.is_alive() != True:
                print("Kill this thread")
                self.close()
                self.active=False

