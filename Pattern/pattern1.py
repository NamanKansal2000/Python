def pattern(number):
    n = number
    ls = []

    for i in range(0, n):
        ls.append('*' * i)
    for i in range(0, n):
        print(ls[i], end='\n')


n = input()
pattern(int(n))
