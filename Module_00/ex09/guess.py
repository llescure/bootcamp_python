import random
import sys


random_number = random.randint(1, 99)
count_attempts = 1
if len(sys.argv) != 1:
    print("ERROR usage: python3 guess.py")
    exit()
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret" +
      "number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")
while (1):
    number_guessed = input("What's your guess between 1 and 99?\n")
    if number_guessed == "exit":
        print("Goodbye!")
        exit()
    try:
        int(number_guessed)
        if int(number_guessed) == random_number:
            if random_number == 42:
                print("The answer to the ultimate question of life, the" +
                      "universe and everything is 42.")
            if count_attempts == 0:
                print("Congratulations! You got it on your first try!")
                break
            else:
                print("Congratulations, you've got it!")
                print("You won in %d attempts!" % (count_attempts))
                break
        elif int(number_guessed) > random_number:
            print("Too high!")
        elif int(number_guessed) < random_number:
            print("Too low!")
    except ValueError:
        print("That's not a number.")
    count_attempts += 1
