print("This code tells if a no is even or odd")

while True:

    num = (input("Enter a no: "))
    num = num.lower()
    if num in ['y', 'yes', 'done', 'n', 'no']:
        break
    else:
        num = int(num)
        if num % 2 == 0:
            print("No is Even")
            if num % 4 == 0:
                print("No is a multiple of 4 too")
        else:
            print("No is odd")

print("Enter two no's to check if first is a factor of other")
num = int(input("Enter no 1: "))
check = int(input("Enter no 2: "))
if num % check == 0:
    print(check + " is a factor of " + num)
else:
    print(check + " is not a factor of " + num)
