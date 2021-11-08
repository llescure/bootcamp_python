import string


def text_analyzer(*args):

    if len(args) == 0:
        text = input("What is the text to analyse?")
    elif len(args) > 1:
        print("ERROR")
        return
    else:
        text = args[0]
    if text == '':
        print("Text empty")
        return
    number_characters = len(text)
    number_upper_letters = sum(1 for c in text if c.isupper())
    number_lower_letters = sum(1 for c in text if c.islower())
    number_spaces = sum(1 for c in text if c.isspace())
    number_punctuation_marks = sum(1 for c in text if c in string.punctuation)
    print("The text contains %d characters" % number_characters)
    print("- %d upper letters" % number_upper_letters)
    print("- %d lower letters" % number_lower_letters)
    print("- %d punctuation marks" % number_punctuation_marks)
    print("- %d spaces" % number_spaces)
    return
