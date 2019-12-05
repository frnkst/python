# Usage: python3 22_async_response_times.py -u https://www.cnn.com -n 80
#
# Note: The limit for OSX is 256 parallel connections (https://stackoverflow.com/questions/7578594/how-to-increase-limits-on-sockets-on-osx-for-load-testing)
# Async: https://skipperkongen.dk/2016/09/09/easy-parallel-http-requests-with-python-and-asyncio/

import asyncio
import requests
import curses
import argparse


async def main():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None,
            requests.get,
            args.url
        )
        for i in range(int(total_requests))
    ]

    for future in futures:
        future.add_done_callback(print_inflight_update)

    # Wait for all the responses (aka Promise.all)
    responses = await asyncio.gather(*futures)

    # Calculate metrics
    average_response_time = sum(i.elapsed.total_seconds() for i in responses) / total_requests
    max_time = max(i.elapsed.total_seconds() for i in responses)
    min_time = min(i.elapsed.total_seconds() for i in responses)

    # Display final results
    scr.addstr(5, 0, "Average: %.2f seconds" % average_response_time)
    scr.addstr(6, 0, "Minimum: %.2f seconds" % min_time)
    scr.addstr(7, 0, "Maximum: %.2f seconds" % max_time)
    scr.addstr(9, 0, "Hit enter to exit \n")
    scr.refresh()

    # Exit on enter
    c = scr.getch()
    if c == curses.KEY_ENTER or c == 10 or c == 13:
        curses.endwin()


def print_inflight_update(future):
    global total_responses, total_OK, total_ERROR
    total_responses += 1

    status_code = future.result().status_code
    if status_code == 200:
        total_OK += 1
    elif status_code >= 400:
        total_ERROR += 1

    scr.addstr(0, 0, "Sending %d requests to %s" % (total_requests, args.url))
    scr.addstr(2, 0, "Requests sent: " + str(total_requests))
    scr.addstr(3, 0, "Responses received: %d (OK: %d, Error: %d)" % (total_responses, total_OK, total_ERROR))
    scr.refresh()


parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True, help="request url")
parser.add_argument('-n', '--number', required=True, help="the number of parallel requests to be send")
args = parser.parse_args()

total_requests = int(args.number)
total_responses = 0
total_OK = 0
total_ERROR = 0
scr = curses.initscr()

# Need to run the async method in an event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
