import random


def guess(choice):
    num = random.randint(1, 9)
    if choice < num:
        print('Your guess is too low')
    elif choice == num:
        print('You guessed it exactly right')
    else:
        print('Your guess is too high')


while True:
    print('Welcome! to the Guessing Game')
    choice = input('Enter your choice:\n(A number between 1-9)\n--> ')
    if choice == 'exit':
        break
    elif choice < 1 or choice > 9:
        print('Invalid Choice')
        print('Please try again\nElse enter "exit" to exit')
        choice = input('Enter your choice:\n(A number between 1-9)--> \n')
    guess(choice)
