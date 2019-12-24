# Hackerrank: Detect Floating Point Number
import re

# Pattern explanation
# -----------------------------------------------------------------------------
# ^         : Beginning of line
# ?(\+|\-)  : Optional plus or minus (the characters itself need to be escaped)
# ?\d*      : An optional number of digits
# \.        : A dot
# \d*$      : One or multiple digits till the end of line
pattern = r'^?(\+|\-)?\d*\.\d*$'

dummy_in = """
4
4.0O0
-1.00
+4.54
SomeRandomStuff"""

input = dummy_in.split("\n")[1:]

for number in input:
    print(bool(re.match(pattern, number)))
