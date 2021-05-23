n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in reversed(range(n)):
        if j < i:
            print(" ", end="")
        else:
            if i == 0 or j == n-1 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
    print()
