#   My First Game.

import sys          # Importing The sys class
import random       # Importing The random class

names = []          # The List That Stores The Name

try:                 # Simple Exception for when The Person Playing Want's To Exit The Game/Program.
    name = input('\nWhat is your name?: ')              # Name Input
    if name == 'q':
        print(f'\nThank you for playing My First Game')
        sys.exit()
    names.append(name)  # Adding The Name to The List

except IndexError:      # A simple Exception in case of an error.
    print(f'\nThank you for playing My First Game')


# The Simple Message for The Game.
print("\nLet's play a simple Game."
      "\nI am thinking of a number."
      "\nDo you want to guess?"
      "\nIf so Enter you number if not press 'q'.")

secret_number = random.randint(1,10)            # This is how we represent the random secret Number.

try:            # Simple Exception for when The Person Playing Want's To Exit The Game/Program or Presses a Letter.

    while True:

        number = input('\nEnter your number Here: ')         # Asking for the number.

        if number.isdigit() and int(number) == secret_number :          # Using the isdigit() method to check for str()
            print (f'\nYou are Correct, {names[-1].title()}! The Number I was thinking was: {number}!'
                f'\nYou Won!')
            print(f'\nThank you for playing My First Game my lovely {names[-1].title()}!')
            sys.exit()
        elif number.isalpha():          # Using the isalpha() method to prompt the user if they entered a letter.
            if number == 'q':
                print(f'\nThank you for playing My First Game my lovely {names[-1].title()}!')
                break
            if len(number) <= 1:
                print('You have entered a letter please choose a number between 1 and 10.')
            elif len(number) > 1:
                print('You have entered letters please choose a number between 1 and 10.')
        elif int(number) > secret_number:
            print('My number is smaller.')
        elif int(number) < secret_number:
            print('My number is bigger.')
        elif number != secret_number:
            print('Please Try Again by entering another number or type "q" to Quit.')

        elif number == 'q':
            sys.exit()

except ValueError:
    print(f'\nThank you for playing My First Game my lovely {names[-1].title()}!'
          f'\nYou need to Enter a Number not a Letter, try again Later.')
