import random


def display():
    print("Welcome to KBC!!")
    marks = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000,
             320000, 640000, 1250000, 2500000, 5000000, 10000000]
    print()
    print("Max No of available QUESTION are: 16")
    print()
    for i in range(len(marks)):
        print(i + 1, "->", marks[i])
    print()
    print("Press any key to start the game .......")


def prize(i):
    prize = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000,
             320000, 640000, 1250000, 2500000, 5000000, 10000000]
    return prize[i]


def ques_ans():
    ques_no = 1
    ques = [i for i in range(1, 17)]
    choice = []
    count = 0
    for i in range(len(ques)):
        choice.append(['A', 'B', 'C', 'D'])
    # print(choice)
    ans = [random.choice(choice[count]) for i in range(len(ques))]
    flag_flip = 1
    flag_50 = 1
    sum = 0
    while count <= len(ques):
        print("Ques", ques_no, ':-', ans[count])
        print("Options:-")
        for i in choice[count]:
            print(i)
        print("Press L to choose lifeline!!")
        inp = input('Enter Choice:- ')
        inp = inp.upper()
        while True:
            if inp in ['A', 'B', 'C', 'D', 'l', 'L']:
                break
            print('Please try again.......')
            inp = input('Enter Choice:- ')
        if inp in ['l', 'L']:
            if flag_50 == 0 and flag_flip == 0:
                print("You have already used all u r lifelines!!")
                # print("Enter choice:- ")
                inp = input("Enter choice:- ")
                inp = inp.upper()
                while True:
                    if inp in ['A', 'B', 'C', 'D']:
                        break
                    print('Please try again.......')
                    inp = input('Enter Choice:- ')
            else:
                print('Which lifeline do u want to choose: ')
                if flag_50:
                    print('50-50 (press 5)')
                if flag_flip:
                    print('Flip (press F)')
                life_inp = input('Enter Choice:- ')
                while True:
                    if life_inp in ['5', 'f', 'F']:
                        break
                    print('Please try again.......')
                    life_inp = input('Enter Choice:- ')
                if life_inp == '5':
                    flag_50 = 0
                    options = choice_red(ans[count], choice[count])
                    print("Ques", count+1, ':-', ans[count])
                    for i in options:
                        if i != 'Incorrect-Option':
                            print(i)
                    inp = input('Enter Choice:- ')
                    inp = inp.upper()
                    while True:
                        if inp in ['A', 'B', 'C', 'D', 'l', 'L']:
                            break
                        print('Please try again.......')
                        inp = input('Enter Choice:- ')
                if life_inp in ['f', 'F']:
                    flag_flip = 0
                    count += 1
                    continue

        if inp == ans[count]:
            print('Right ans!!!!')
            sum = prize(ques_no - 1  )
            print('You have won Rs', sum)
        else:
            print('Wrong Answer!!')
            print('Congratulations U have Won Rs', sum)
            return None

        count += 1
        ques_no += 1
        print()


def choice_red(ans, ls):
    # ls.remove(ans)
    # res = [ans]
    # res.append(random.choice(ls))
    count = 0
    i = 0
    while(count<2):
        if ls[i] != ans:
            ls[i] = 'Incorrect-Option'
            count += 1
        i += 1
    return ls


display()
val = input()
if val not in ['q', 'Q', 'quit', 'QUIT', 'exit']:
    ques_ans()
