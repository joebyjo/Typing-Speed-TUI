from TypingSpeed import *
from RecordManagement import *
from Utils import *
from datetime import datetime
from os import path

start_art = """
████████╗██╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███████╗██████╗ ███████╗███████╗██████╗ 
╚══██╔══╝╚██╗ ██╔╝██╔══██╗██║████╗  ██║██╔════╝     ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
   ██║    ╚████╔╝ ██████╔╝██║██╔██╗ ██║██║  ███╗    ███████╗██████╔╝█████╗  █████╗  ██║  ██║
   ██║     ╚██╔╝  ██╔═══╝ ██║██║╚██╗██║██║   ██║    ╚════██║██╔═══╝ ██╔══╝  ██╔══╝  ██║  ██║
   ██║      ██║   ██║     ██║██║ ╚████║╚██████╔╝    ███████║██║     ███████╗███████╗██████╔╝
   ╚═╝      ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝ 
                                                                            By: Joe
\n
"""


def TypingSpeed(username):
    """Main TypingSpeed function. includes all front-end logic"""

    string = get_words()
    _string = "\u200e ".join(string)  # get string to be displayed, added zero width char to prevent cheating

    print("Words:\n    " + _string)

    # timer(3)
    sleep(1)

    start_time = datetime.now()
    user_input = input(" —> ")
    end_time = datetime.now()
    timetaken = round((end_time - start_time).total_seconds(), 1)  # calc timetaken and round off

    if "\u200e " in user_input:  # anti-cheat
        print("Nice Try but you can't do that here")
        return

    netWPM = net_wpm(user_input, _string, timetaken)
    grossWPM = gross_wpm(user_input, timetaken)
    Accuracy, errors = accuracy(user_input, _string)

    # Print results

    results = f"""
    Net WPM: {netWPM}     Accuracy: {Accuracy}%    Gross WPM: {grossWPM}
    Time Taken: {timetaken}     Errors: {errors}
    """

    data = {'String': ' '.join(string), 'userInput': user_input, 'timeTaken': timetaken, 'netWPM': netWPM,
            'grossWPM': grossWPM, 'Accuracy': Accuracy, 'Error': errors}  # Data to be sent to update_user_data()
    update_user_data(username, data)
    print(results + "\n")


if __name__ == '__main__':

    # Check if records.dat file exists
    if not path.exists('records.dat'):
        create_file()

    print(start_art)
    username = input("Username: ").strip().lower()  # gets username and removes any extra spaces

    # Menu-driven program
    while True:
        choice = input("    1.Play    2.View My Stats    3.Leaderboard    99.Exit\n\t")
        clear()
        if choice.lower() in ["p", 'play', '1']:
            print(start_art,end='\n\n\n')
            TypingSpeed(username)

        elif choice.lower() in ["r", 'records', 'view records', '2']:
            print(start_art)
            view_records(username)
        elif choice.lower().split()[0] in ["l", 'leaderboard', '3']:
            print(start_art)
            try:
                param = choice.lower().split()[1]
                view_leaderboard()
            except IndexError:
                view_leaderboard()

        elif choice.lower() in ["e", 'exit', '99']:
            break
