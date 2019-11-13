# Sequentially sends a number of requests to a given url
# Usage: python3 05_response_times.py http://www.google.com 20

import requests
import sys

url = sys.argv[1]
number_of_requests = int(sys.argv[2])

print('Sending %s requests to %s. Please wait...' % (number_of_requests, url))

responses = []
for i in range(0, int(sys.argv[2])):
    response = requests.get(sys.argv[1])
    responses.append(response.elapsed.total_seconds())

print('Average: %ss' % round((sum(responses) / len(responses)), 3))
print('Fastest: %ss' % round(min(responses), 3))
print('Slowest: %ss' % round(max(responses), 3))
print('')
print('Total time: %ss' % round(sum(responses), 3))
