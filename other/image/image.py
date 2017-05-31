#!/usr/bin/env python
#-*- coding:utf-8 -*-
#缩小图片
import Image, ImageFilter, ImageFont, ImageFilter, ImageDraw
im= Image.open('./1.bmp')
w, h = im.size
im.thumbnail((w//2, h//2))
im.save('./2.bmp')

#模糊图片
im = Image.open('./1.bmp')
im2 = im.filter(ImageFilter.BLUR)
im2.save('./3.bmp')

#PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
import random

#随机字母：
def rndChar():
    return chr(random.randint(65, 115))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
fonts=5
width = 60 * fonts
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(fonts):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg');

