import sys

only_string = ''
combined_string = ''
i = len(sys.argv) - 1
while i > 0:
    only_string = sys.argv[i][::-1]
    only_string = only_string.swapcase()
    if len(sys.argv) > 2 & i > 1:
        combined_string += only_string + ' '
    elif i == i:
        combined_string += only_string
    i -= 1
if len(sys.argv) == 2:
    print(only_string)
elif len(sys.argv) > 2:
    print(combined_string)
