# Extracts a color palette from a given link to an image, and paints lines with that color palette.
# Usage example: python3 16_draw_circles.py -u https://data.whicdn.com/images/247170900/original.jpg -w 20

from haishoku.haishoku import Haishoku
from PIL import Image, ImageDraw
import random
from random import randrange
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True, help="url to the image")
parser.add_argument('-w', '--width', required=True, help="the line width")
args = parser.parse_args()

line_width = int(args.width)

palette = Haishoku.getPalette(args.url)
w, h = 800, 800

image = Image.new("RGB", (w, h), random.choice(palette)[1])
layer = ImageDraw.Draw(image)

x = 0
for i in range(0, w, line_width):
    x = x + line_width
    r,g,b = random.choice(palette)[1]

    if randrange(0, (randrange(2, 20))) == 1:
        color = "rgb(" + str(r) + "," + str(g) + "," + str(b) + ")"
        layer.rectangle((x, 0, x + line_width * (randrange(1, 10)), h), fill=color)

y = 0
for i in range(0, w, line_width):
    y = y + line_width
    r,g,b = random.choice(palette)[1]

    if randrange(0, (randrange(2, 20))) == 1:
        color = "rgb(" + str(r) + "," + str(g) + "," + str(b) + ")"
        layer.rectangle((0, y, w, y + line_width * (randrange(1, 10))), fill=color)

image.show()
