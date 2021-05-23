import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")


def rock_paper_scissor(str):
    print('Your choice: ' + str)
    comp = random.randint(0, 2)
    if comp == 0:
        print('Computer Choice: rock')
    elif comp == 1:
        print('Computer Choice: paper')
    elif comp == 2:
        print('Computer Choice: scissor')
    if str == 'rock':
        sel = 0
    elif str == 'paper':
        sel = 1
    elif str == 'scissor':
        sel = 2
    else:
        print('Invalid Entry')

    if (sel - comp) == 1:
        print('You Win')
    elif sel == comp:
        print('Its a tie')
    else:
        print('Computer Wins')


while True:
    print("Enter choice \n 1. rock \n 2. paper \n 3. scissor \n")
    choice = int(input("User turn: "))
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    rock_paper_scissor(choice)
