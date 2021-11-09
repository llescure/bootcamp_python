import sys
import re


def filter_function(string, lenght):
    new_list = []
    str_split = re.split(r"\W+", string)
    for word in str_split:
        if len(word) > lenght:
            new_list.append(word)
    print(new_list)


if len(sys.argv) != 3:
    print("ERROR")
else:
    try:
        string = str(sys.argv[1])
        lenght = int(sys.argv[2])
        filter_function(string, lenght)
    except ValueError:
        print("ERROR")
