print("This is a guessing game played by computer")
print("Think a no in range (1,100) \nComputer will guess and tell its choice "
      + "you have to tell if no is high or low")


def guess_():
    start_choice = 1
    end_choice = 100

    count = 0
    while True:
        count += 1
        choice = (end_choice + start_choice)//2
        print("Computer's Guess == ", (choice))
        str = input("Enter wether computer guess is: \n1. low\n2. high\n3. "
                    + "equal\n")
        if choice < 1 or choice > 100:
            print("Try again")
            return None
        elif str == 'low':
            start_choice = choice
        elif str == 'equal':
            print("Computer: Yeeeee i finally guessed! after ", count, " turns"
                  )
            return None
        elif str == "high":
            end_choice = choice


guess_()
