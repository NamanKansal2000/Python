print("This code prints all the divisor of entered number")
num = int(input("Enter the number"))
divisor = []
for i in range(1, num+1):
    if num % i == 0:
        divisor.append(i)
print(divisor)
