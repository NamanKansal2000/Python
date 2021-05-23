import datetime
name = input('Enter your name: ')
print("Your name is " + name)
age = int(input('Enter your age: '))
year = datetime.date.today().year + 100 - age

print("You will turn 100 in " + str(year))

# copy the program no of times
num = int(input("Enter a no to copy the printed text that many times: "))
print(("You will turn 100 in " + str(year) + '\n')*num)
