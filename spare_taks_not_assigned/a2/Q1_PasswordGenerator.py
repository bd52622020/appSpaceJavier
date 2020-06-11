import string
import random

print('Welcome to the password generator')
l = int(input('How long would you like to have your password: ')) - 2


# Get all chars
LETTERS = string.ascii_letters
NUMBERS = string.digits  
PUNCTUATION = string.punctuation    

# Combine chars
chars = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

chars = list(chars)
random.shuffle(chars) # Shuffle all the list

random_password = random.choices(chars, k=l)
random_password = ''.join(random_password)

print('Your random password is' + random_password)
