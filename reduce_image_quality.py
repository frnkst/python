# Reduces image quality to 90%
# Usage: python3 reduce_image_quality.py *.JPG

import os.path
from sys import argv
from PIL import Image

for file_path in argv[1:]:
    try:
        image = Image.open(file_path)
    except IOError as e:
        print("Error opening %s: %s" % (file_path, e))
        continue

    print("Processing %s" % file_path)
    quality_val = 90
    file_name, extension = os.path.splitext(file_path)
    image.save(file_name + "_changed.jpg", 'JPEG', quality=quality_val)
