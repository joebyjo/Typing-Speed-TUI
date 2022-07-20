from random import choice


def get_words():
    """
    Get words from word_list.txt file which returns a
    random selection of 5 words in the form of a list
    """

    word_list_file = "word_list.txt"

    # get words from word_list.txt
    with open(word_list_file,"r") as f:
        word_list = f.read()
        word_list = word_list.split("\n")

    words = []
    # choose 5 random words from word_list and append to words if its not there
    for i in range(5):
        word = choice(word_list)
        if word not in words:
            words.append(word)

    return words


def accuracy(input_text, text):
    """
    calculates accuracy of typing speed by comparing
    input_text and text on the basis of number of errors
    """

    # remove anti-cheat char from text
    text = text.replace("\u200e ", " ")
    error = 0

    text_lst = text.split()
    inp_lst = input_text.split()

    for i, c in enumerate(text_lst):
        for itr, cont in enumerate(c):
            try:
                if inp_lst[i][itr] == cont:
                    continue

                elif inp_lst[i][itr] != cont:
                    error += 1

            except IndexError:
                pass

    if len(input_text) > len(text):
        error += 2 * (len(input_text) - len(text))

    accuracy = ((len(input_text) - error) / len(text)) * 100

    if accuracy < 0:
        accuracy = 0.0

    return round(accuracy), error


def gross_wpm(input_text, total_time):
    """
    returns gross_wpm(wpm without accounting for errors)
    formula:
        length of input_text x 60
        —————————————————————————
             5  x  time_taken

    """
    wpm = len(input_text) * 60 / (5 * total_time)
    return round(wpm)


def net_wpm(input_text, text, total_time):
    """
    returns net_wpm(wpm accounting for errors)
    formula:
        (length of input_text - errors) x 60
        ————————————————————————————————————
                 5   x   time_taken

    """

    errors = (accuracy(input_text, text))[1]
    wpm = ((len(input_text) - errors) * 60) / (total_time * 5)
    if wpm > 0:
        return round(wpm)
    else:
        return 0


if __name__ == '__main__':
    print(get_words())
