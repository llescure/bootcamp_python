import random


def error_case(text, option):
    text_is_str = isinstance(text, str)
    if text_is_str is False:
        return -1
    if option is not None and option is not "shuffle" and option is not \
            "ordered" and option is not "unique":
        return -1
    return 0


def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""
    if error_case(text, option) == -1:
        print("ERROR")
        return
    str = text.split(sep)
    if option is None:
        for words in str:
            yield words
    elif option == "shuffle":
        new_list = random.sample(str, len(str))
        for words in new_list:
            yield words
    elif option == "ordered":
        for words in sorted(str):
            yield words
    elif option == "unique":
        for words in list(dict.fromkeys(str)):
            yield words
