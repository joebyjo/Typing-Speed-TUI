from time import sleep


def timer(seconds):
    """starts a timer for n seconds"""

    for i in range(seconds, 0, -1):
        print(f'{i}', end='')
        sleep(0.2)
        for j in range(4):
            print('.', end='')
            sleep(0.2)

    print('GO!')


def clear(n=50):
    """clears the terminal with n newline characters"""
    print('\n'*n)


def average(lst):
    """returns average of elements of a provided list"""
    _sum = sum(lst)
    _len = len(lst)
    return round(_sum/_len,1)


def render_table(headers, data):
    """
    prints provided dict() in the form of a clean and readable table

    headers = ("username","Net WPM","Accuracy")
    [{"username": "xyz", "Net WPM": 70, "Time taken": 4,"Accuracy":100}]

    ┌───────────────────────────────┐
    ⏐ USERNAME ⏐ NET WPM ⏐ ACCURACY ⏐
    ├───────────────────────────────┤
    │   xyz    │   70    │    100   │
    └───────────────────────────────┘

    """

    num_of_columns = 0
    head = ''
    for header in headers:
        greatest_value = max([len(str(x[header])) for x in data])  # find cell in column with greatest length

        # print headers one-by-one
        head += '│ '
        header = header.center(greatest_value).upper()
        head += header + ' '

        num_of_columns += len(header) + 3
    head += '│'

    print('┌' + ('─' * (num_of_columns - 2)) + '─┐')
    print(head)
    print('├' + ('─' * (num_of_columns - 2)) + '─┤')

    # print data one-by-one
    for item in data:
        for header in headers:
            stats = str(item[header])
            greatest_value = max([len(str(x[header])) for x in data])

            greatest_value = greatest_value if greatest_value > len(header) else len(header)  # reassign greatest_value to longest value in entire column to center data

            print('│ ', end='')
            print(stats.center(greatest_value), end=' ')  # center data
        print('│')
    print('└' + ('─' * (num_of_columns - 2)), end='─┘\n')

    print('\n'*3)


if __name__ == '__main__':
    # Used during developement

    headers = ('userInput', 'timeTaken', 'netWPM', 'grossWPM', 'Accuracy', 'Error')

    data = [{'String': 'premium hang capricious ancient mysterious', 'userInput': 'premium hang capricious ancient mysterious', 'timeTaken': 10.4, 'netWPM': 48, 'grossWPM': 48, 'Accuracy': 100, 'Error': 0},
            {'String': 'governor utter vacuous bulb test', 'userInput': 'governor utter vacous bulb test', 'timeTaken': 7.2, 'netWPM': 47, 'grossWPM': 52, 'Accuracy': 88, 'Error': 3},
            {'String': 'prevent education obese changeable fade', 'userInput': 'prevent education obese changeable fade', 'timeTaken': 7.5, 'netWPM': 62, 'grossWPM': 62, 'Accuracy': 100, 'Error': 0}]

    # headers = ("username", 'time', 'netwpm', 'grosswpm','accuracy')
    # data = [
    #     {'username': 'joe', 'time': 4, 'netwpm': 70, 'grosswpm': 70,'accuracy':100},
    #     {'username': 'joe', 'time': 4, 'netwpm': 70, 'grosswpm': 70,'accuracy':100},
    #     {'username': 'joe', 'time': 4, 'netwpm': 70, 'grosswpm': 70,'accuracy':100},
    # ]

    render_table(headers, data)

    timer(3)
    clear()