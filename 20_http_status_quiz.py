from bs4 import BeautifulSoup
import lxml
import requests
import random
from PyInquirer import prompt
from examples import custom_style_2


def get_number_of_rounds():
    questions = [
        {
            'type': 'list',
            'name': 'amount',
            'message': 'How many question you want to solve?',
            'choices': [
                '5',
                '10',
                '20',
                '50',
                '100'
            ]
        }
    ]
    return int(prompt(questions, style=custom_style_2)['amount'])


def get_all_status_codes():
    r = requests.get("https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml")
    soup = BeautifulSoup(r.content, 'lxml')
    rows = soup.find("table", id="table-http-status-codes-1").find("tbody").find_all("tr")
    status_codes = []
    for row in rows:
        status_code, name, link = row.find_all("td")
        if name.text != "Unassigned" and name.text != "(Unused)":
            status_codes.append((status_code.text, name.text, link.text))
    return status_codes


def print_results(score, wrongs):
    print("")
    print("------------------------")
    print("")
    print("You answered %s out of %s correctly" % (score, number_of_rounds))
    print("")
    print("The wrong ones were:")

    mdn_link = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/"
    for wrong in list(set(wrongs)):
        code, name, link = wrong
        print("%s - %s (%s)" % (code, name, mdn_link + code))


number_of_rounds = get_number_of_rounds()
print("Alright, let's get started. What is the status code for the following: ")

score = 0
wrongs = []
status_codes = get_all_status_codes()
for i in range(0, number_of_rounds):
    code, name, link = random.choice(status_codes)
    input_code = input(name + " : ")
    if input_code == code:
        score += 1
    else:
        print("Wrong. The correct answer is: %s" % code)
        wrongs.append((code, name, link))

print_results(score, wrongs)
