def fibo(n):
    """ Print fibonacci series till input n"""
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


# fibo(input('Enter till u want to generate fibonacci series'))
fibo(2000)
