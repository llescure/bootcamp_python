import sys


eng_to_morse = {
                'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
                'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
                'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--',
                'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
                'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-',
                'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',  ' ': '/',
                '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                '9': '----.', '0': '-----'
}

morse_code = ""
i = 1
if (len(sys.argv) == 1):
    exit()
while i < len(sys.argv):
    lower_case_words = sys.argv[i].lower()
    if i != 1:
        morse_code += " " + eng_to_morse[" "] + " "
    for letter in lower_case_words:
        if letter.isalnum() == 0 and letter != " ":
            print("ERROR")
            exit()
        if letter == " ":
            morse_code += " " + eng_to_morse[letter] + " "
        else:
            morse_code += eng_to_morse[letter]
    i += 1
print(morse_code)
