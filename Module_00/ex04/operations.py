import sys


def make_operations(first_number, second_number):
    sum_numbers = first_number + second_number
    difference_numbers = first_number - second_number
    product_numbers = first_number * second_number
    print("Sum:        %d" % sum_numbers)
    print("Difference: %d" % difference_numbers)
    print("Product:    %d" % product_numbers)
    if second_number == 0:
        print("Quotient:   ERROR (div by zero)")
        print("Remainder:  ERROR (modulo by zero)")
    else:
        print("Quotient:  ", first_number / second_number)
        print("Remainder: ", first_number % second_number)
    return


if len(sys.argv) < 3:
    print("Usage: python operations.py <number 1> <number 2>")
    print("Example:")
    print("python operations.py 10 3")
elif len(sys.argv) > 3:
    print("InputError: too many arguments")
    print("Usage: python operations.py <number 1> <number 2>")
    print("Example:")
    print("python operations.py 10 3")
else:
    try:
        first_number = int(sys.argv[1])
        second_number = int(sys.argv[2])
        make_operations(first_number, second_number)
    except ValueError:
        print("InputError: only numbers")
        print("")
        print("Usage: python operations.py <number 1> <number 2>")
        print("Example:")
        print("python operations.py 10 3")
