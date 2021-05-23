import random


with open('sowpods.txt') as fhand:
    line = fhand.read()

line = line.split('\n')


def random_word():
    choice = random.choice(line)
    print(choice)


random_word()
