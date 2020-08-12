from haishoku.haishoku import Haishoku
from PIL import Image, ImageDraw
import random
from random import randrange
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True, help="url to the image")
parser.add_argument('-a', '--amount', required=True, help="the amount of circles")
parser.add_argument('-r', '--radius', required=True, help="the max radius")
args = parser.parse_args()

palette = Haishoku.getPalette(args.url)
w, h = 1200, 1200

image = Image.new("RGB", (w, h), random.choice(palette)[1])
layer = ImageDraw.Draw(image)

for i in range(0, int(args.amount)):
    r,g,b = random.choice(palette)[1]
    color = "rgb(" + str(r) + "," + str(g) + "," + str(b) + ")"
    x = randrange(w)
    y = randrange(h)
    radius = randrange(0, int(args.radius))
    layer.ellipse((x, y, x + radius, y + radius), fill=color)

image.show()
