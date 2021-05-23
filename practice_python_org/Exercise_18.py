import random

print("This code is a guessing game\nFor every digit that the user guessed "
      + "correctly in the correct place, they have a “cow”. \nFor every digit "
        + "user guessed correctly in the wrong place is a “bull.”")
num = random.randint(1000, 9999)
num = str(num)
choice = input("Enter you choice: ")
print("Computer's Choice is: " + num)
cows = 0
bulls = 0
for i in range(4):
    if choice[i] == num[i]:
        cows += 1
    elif choice[i] in num:
        bulls += 1

print("No of cows: " + str(cows) + "\nNo of bulls: "+str(bulls))
