from sys import argv
from pyzbar.pyzbar import decode
from PIL import Image

print(decode(Image.open(argv[1])))
