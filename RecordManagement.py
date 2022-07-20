from pickle import dump, load
from Utils import *

RECORD_FILE = "records.dat"


def create_file(file_name=RECORD_FILE):
    """create .dat file to store all user data"""
    with open(file_name, 'wb') as f:
        data = {}
        dump(data, f)


def create_user(username):
    """create user in records file with all headers"""
    with open(RECORD_FILE, "rb") as read_f:
        existing_data = load(read_f)

    num = list(existing_data)
    uid = 100 if len(num) == 0 else num[-1] + 1

    data = {"username": username,
            "highscore_nWPM": 0,
            "highscore_gWPM": 0,
            "highscore_time": 100,
            "average_WPM": 0,
            "average_time": 0,
            "average_accuracy": 0,
            "data": []
            }

    existing_data[uid] = data

    with open(RECORD_FILE, "wb") as write_f:
        dump(existing_data, write_f)


def update_user_data(username, data):
    """update record file with new data"""

    with open(RECORD_FILE, "rb") as read_f:
        existing_data = load(read_f)

    members = {existing_data[uid]["username"]: uid for uid in existing_data}

    # print(members)
    if username in members.keys():

        existing_data[members[username]]['highscore_nWPM'] = data["netWPM"] if data["netWPM"] > existing_data[members[username]]['highscore_nWPM'] else existing_data[members[username]]['highscore_nWPM']
        existing_data[members[username]]['highscore_gWPM'] = data["netWPM"] if data["grossWPM"] > existing_data[members[username]]['highscore_gWPM'] else existing_data[members[username]]['highscore_gWPM']
        existing_data[members[username]]['highscore_time'] = data["timeTaken"] if data["timeTaken"] < existing_data[members[username]]['highscore_time'] else existing_data[members[username]]['highscore_time']

        existing_data[members[username]]['data'].append(data)

        existing_data[members[username]]['average_WPM'] = average([data["netWPM"] for data in existing_data[members[username]]["data"]])
        existing_data[members[username]]['average_time'] = average([data["timeTaken"] for data in existing_data[members[username]]["data"]])
        existing_data[members[username]]['average_accuracy'] = average([data["Accuracy"] for data in existing_data[members[username]]["data"]])

        with open(RECORD_FILE, "wb") as write_f:
            dump(existing_data, write_f)

    elif username not in members.keys():
        create_user(username)
        update_user_data(username, data)


def view_all_data(file_name=RECORD_FILE):
    """view all data from record file. used during development"""
    with open(file_name, "rb") as f:
        return load(f)


def view_records(username):
    """view user data in clean and readable table"""
    with open(RECORD_FILE, "rb") as f:
        data = load(f)

    members = {data[uid]["username"]: uid for uid in data}
    if username not in members.keys():
        print("Error: User Does Not exist")
        return

    user = data[members[username]]

    highscore_nWPM = user['highscore_nWPM']
    highscore_gWPM = user['highscore_gWPM']
    highscore_time = user['highscore_time']
    average_wpm = user['average_WPM']
    average_time = user['average_time']
    average_accuracy = user['average_accuracy']

    print(f'''
       Best Net-WPM: {highscore_nWPM}       Best-Gross WPM : {highscore_gWPM}          Best-Time    : {highscore_time}
    Average Net-WPM: {'%4s'%average_wpm}      Average Time  :{'%4s'%average_time}s    Average Accuracy : {'%4s'%average_accuracy}%
''')

    headers = ('userInput', 'timeTaken', 'netWPM', 'grossWPM', 'Accuracy', 'Error')
    render_table(headers, user['data'])



def view_leaderboard(key='highscore_nWPM'):
    """view leaderboard in clean and readable table sorted by any argument"""

    with open(RECORD_FILE, "rb") as f:
        data = load(f)

    def sort_wpm(data):
        return data[key]

    data = sorted([data[user] for user in data],key=sort_wpm,reverse=False if 'time' in key else True)
    headers = ('username', 'highscore_nWPM', 'highscore_gWPM', 'highscore_time', 'average_time', 'average_accuracy')

    render_table(headers, data)


if __name__ == "__main__":
    # create_file(RECORD_FILE)
    # create_user("bruh")

    '''add dummy data'''
    # data = {
    #         "String":"gruesome abject able nonstop attend",
    #         "userInput":"gruesome abject able nonstop attend",
    #         "timeTaken":6.1,
    #         "netWPM":61,
    #         "grossWPM":61,
    #         "Accuracy":100,
    #         "Error":0
    #      }
    # update_user_data('joe', data)


    # view_leaderboard()
    # print(view_all_data(RECORD_FILE))

    '''delete last record of user with id 100'''
    # x = view_all_data(RECORD_FILE)
    # x[100]['data'].pop(-1)
    # with open(RECORD_FILE, "wb") as write_f:
    #     dump(x, write_f)

    view_records('joe')
