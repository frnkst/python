# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys

input = "t   aaa   t"

pattern = r'(Q|W|R|T|Y|P|S|D|F|G|H|J|K|L|Z|X|C|V|B|N|M|q|w|r|t|y|p|s|d|f|g|h|j|k|l|z|x|c|v|b|n|m)((\s|\+|\-)*)?(P<name>(A|E|I|O|U|a|e|i|o|u){2,})((\s|\+|\-)*)?(Q|W|R|T|Y|P|S|D|F|G|H|J|K|L|Z|X|C|V|B|N|M|q|w|r|t|y|p|s|d|f|g|h|j|k|l|z|x|c|v|b|n|m)'

matches = re.finditer(pattern, input)
x = re.match(pattern, input)
print('x is: ', x.groups('name'))

print(matches)
for match in matches:
    start, end = match.span()
    input[start + 1: end - 1]
    print(input[start+1: end-1])
