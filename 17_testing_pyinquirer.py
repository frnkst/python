from pprint import pprint
from PyInquirer import prompt
from examples import custom_style_2


def get_options(answers):
    options = []
    if answers['mood'] == 'great':
        options.append('Because the world is awesome')
        options.append('Because I\'m awesome')
    if answers['mood'] == 'it\'s ok':
        options.append('Because everything is ok')
        options.append('Because I don\'t care')
    if answers['mood'] == 'terrible':
        options.append('Because it\'s Monday')
        options.append('Don\'t ask me why')
    return options


questions = [
    {
        'type': 'list',
        'name': 'mood',
        'message': 'How do you feel today?',
        'choices': [
            'Great',
            'It\'s ok',
            'Terrible'
        ],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'reason',
        'message': 'Why is that?',
        'choices': get_options,
    },
]

answers = prompt(questions, style=custom_style_2)
pprint(answers)
