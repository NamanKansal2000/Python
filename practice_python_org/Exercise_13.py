def fibo(num):
    count = 0
    a = 0
    b = 1
    ls = []
    while count <= num:
        a, b = b, b + a
        ls.append(a)
        count += 1

    print(ls)


num = int(input('Enter no of Fibonnaci Numbers to be printed: '))
fibo(num)
