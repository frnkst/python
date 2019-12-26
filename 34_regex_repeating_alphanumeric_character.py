# Hackerrank: Group(), Groups() & Groupdict()
# Print the first repeating, alphanumeric character (otherwise -1)
import re

pattern = r'([A-Z]|[a-z]|[0-9])\1'

input = "__test1234556789a"
m = re.search(pattern, input)

if bool(m) is True:
    start, _ = m.span()
    print(input[start: start+1])
else:
    print(-1)
