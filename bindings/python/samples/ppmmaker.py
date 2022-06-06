# import os
# from PIL import ImageFont
# from PIL import Image
# from PIL import ImageDraw

# # text = (("Create", (255, 0, 0)), (" and ", (0, 255, 0)), ("Adafruit", (0, 0, 255)))


# # font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
# # all_text = ""
# # for text_color_pair in text:
# #     t = text_color_pair[0]
# #     all_text = all_text + t

# # print(all_text)
# # width, ignore = font.getsize(all_text)
# # print(width)


# im = Image.new("RGB", (64, 48), (255,0,255))
# draw = ImageDraw.Draw(im)
# draw.text((0, 0, 31, 47), fill=(255, 0, 0))

# # x = 0;
# # for text_color_pair in text:
# #     t = text_color_pair[0]
# #     c = text_color_pair[1]
# #     print("t=" + t + " " + str(c) + " " + str(x))
# #     draw.text((x, 0), t, c, font=font)
# #     x = x + font.getsize(t)[0]

# im.save("0206.png")
# print(im)

from PIL import Image, ImageDraw, ImageFont

# create an image
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


for v in range(10,63):
    for b in range(10,41):
        coordinate = x,y = v,b
        coordinate2= x,y = v,b-25
        col=out.getpixel(coordinate) #get pixel from the current picture
        print (out.getpixel(coordinate)) #print pixel from the current picture
        tmp.putpixel(coordinate2,col) #draw pixel from input picture


tmp.save("tmp.png")

# tmp=Image.new("RGB",(96,32),(0,0,0))
# for 