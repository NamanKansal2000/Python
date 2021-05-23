l = int(input("Enter length of rectange: "))
b = int(input("Enter breadth of rectange: "))
for i in range(b):
    for j in range(l):
        if j == 0 or i == 0 or j == l-1 or i == b-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
