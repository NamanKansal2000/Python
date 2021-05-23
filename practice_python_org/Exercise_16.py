# Random password generator
import string
import random


def password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return (''.join(random.choice(chars) for i in range(length)))


print('This code gives the random generated password')
length = int(input('Enter the length of password: '))
