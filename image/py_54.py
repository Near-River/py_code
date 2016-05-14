#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter


# Image: PIL
def operate():
    # open an image
    im = Image.open('../io/cat.jpg')
    # access the attributes of the image
    w, h = im.size
    print('Original image size: %s x %s' % (w, h))
    # scaling to 50%
    im.thumbnail((w//2, h//2))
    print('Resize image to: %sx%s' % (w//2, h//2))
    # save the scaled image
    im.save('little_cat.jpg', 'jpeg')


def operator2():
    im = Image.open('../io/cat.jpg')
    # apply ImageFilter: blur
    im2 = im.filter(ImageFilter.BLUR)
    im2.save('blur.jpg', 'jpeg')


if __name__ == '__main__':
    # operate()
    operator2()
