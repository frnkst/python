import img2pdf
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', required=True, help="the image to convert")
parser.add_argument('-o', '--output_file', required=True, help="the name of the output pdf")
args = parser.parse_args()

image = Image.open(args.image)
bytes = img2pdf.convert(image.filename)
file = open(args.output_file, "wb")
file.write(bytes)
image.close()
file.close()
