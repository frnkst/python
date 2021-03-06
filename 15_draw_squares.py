# Extracts a color palette from a given link to an image, and paints squares with that color palette.
# Usage example: python3 15_draw_squares.py -u https://data.whicdn.com/images/247170900/original.jpg -a 7810 -r 110

from haishoku.haishoku import Haishoku
from PIL import Image, ImageDraw
import random
from random import randrange
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True, help="url to the image")
parser.add_argument('-a', '--amount', required=True, help="the amount of squares")
parser.add_argument('-r', '--radius', required=True, help="the max radius")
args = parser.parse_args()

palette = Haishoku.getPalette(args.url)
w, h = 800, 800

image = Image.new("RGB", (w, h), random.choice(palette)[1])
layer = ImageDraw.Draw(image)

for i in range(0, int(args.amount)):
    x = randrange(w)
    y = randrange(h)

    r,g,b = random.choice(palette)[1]

    divider = 800 - randrange(0, 600)

    if x >= divider:
        r = r + randrange(100, 200)
    elif y >= divider:
        b = b + randrange(100, 200)

    color = "rgb(" + str(r) + "," + str(g) + "," + str(b) + ")"
    radius = randrange(10, int(args.radius))
    layer.rectangle((x, y, x + radius, y + radius), fill=color)

image.show()
