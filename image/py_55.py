#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


# Image: PIL
# create random character
def rndChar():
    return chr(random.randint(65, 90))


# create random color for background
def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# create random color for text
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def drawImage():
    # 240 x 60:
    width, height = 60 * 4, 80
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # create Font object
    font = ImageFont.truetype('Brown Fox.ttf', 36)
    # create Draw object
    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')


if __name__ == '__main__':
    drawImage()
