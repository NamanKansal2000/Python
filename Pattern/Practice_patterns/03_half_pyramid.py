n = int(input("Enter height of pyramid: "))
for i in range(n):
    for j in range(n):
        if j <= i:
            print("*", end="")
    print()
