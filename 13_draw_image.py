# Far from perfect. Extracts a color palette from a given link to an image
# and tries to draw some rectangles. To be continued ;)

from haishoku.haishoku import Haishoku
from PIL import Image, ImageDraw
import random
from random import randrange

image = "https://image.freepik.com/free-vector/cool-colors-abstract-hand-painted-background_23-2148293333.jpg"

palette = Haishoku.getPalette(image)
w, h = 800, 800

img = Image.new("RGB", (w, h))
img1 = ImageDraw.Draw(img)

for i in range(0, 30):
    print(random.choice(palette)[1])
    r,g,b = random.choice(palette)[1]

    color = "rgb(" + str(r) + "," + str(g) + "," + str(b) + ")"

    endx = randrange(1)
    endy = randrange(1)

    r1 = randrange(w)
    r2 = randrange(h)

    shape = [(i * h,  i * w), (i, 5)]

    img1.rectangle(shape, fill=color, outline=color)

img.show()

