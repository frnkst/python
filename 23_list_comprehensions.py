import numpy as np
import requests


def get_random_list():
    return np.random.choice(20, 20, replace=True).tolist()


print("Basic map function (power to two): ", [x ** 2 for x in get_random_list()])
print("Map with string conversion: ", ["value is: " + str(x) for x in get_random_list()])
print("Filter (greater than 10): ", [x for x in get_random_list() if x > 10])
print("Filter (only evens): ", [x for x in get_random_list() if x % 2 == 0])
print("Filter (only odds): ", [x for x in get_random_list() if x % 2 != 0])
print("Make it unique by using a set comprehension (only odds): ", {x for x in get_random_list() if x % 2 != 0})
# But for reduce a list comprehension is not the best solution
# https://stackoverflow.com/questions/24410420/python-can-reduce-be-translated-into-list-comprehensions-like-map-lambda-and
print("Reduce (better use the reduce function with a lambda")
print("Creating a new list: ", [x for x in range(10)])
print("Sending some requests without a loop: ", [requests.get("https://www.20min.ch").status_code for i in range(2)])
print("Extract every first letter of word: ", ''.join([word[0] for word in ['This', 'is', 'a', 'test']]))
print("Convert all words to lower case: ", [word.lower() for word in ['This', 'is', 'a', 'test']])
print("Extract digits from a string: ", ''.join([x for x in "There are some 123456 digits and some more digits 567" if x.isdigit()]))
print("Multiple arguments: ", [a + b for a in [10, 20, 30] for b in [1, 2, 3]])
print("Going bananas: ", [(url + "/" + path, requests.get(url + "/" + path).status_code) for url in ["https://www.cnn.com", "https://www.20min.ch", "https://www.blick.ch"] for path in ["test", "admin", "bla"]])
print("Bananas but unique: ", {requests.get(url + "/" + path).status_code for url in ["https://www.cnn.com", "https://www.20min.ch", "https://www.blick.ch"] for path in ["test", "admin", "bla"]})
print("New list with tuples: ", [(x, x**2) for x in range(10)])
print("Simple dictionary comprehension: ", {"key_" + str(i): i ** 2 + (i + 1 / 77 - i) for i in range(10, 15, 2)})

# Python 3.8
# print("Using walrus operator:", [url for url in ["https://www.cnn.com", "https://www.20min.chh" if (url := requests.get(url).status_code == 200)])