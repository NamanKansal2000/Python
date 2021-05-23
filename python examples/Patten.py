n = input('Enter no of rows and column')
k = n.split()
n = int(k[0])
m = int(k[1])
if n % 2 != 0 and m == 3*n:
    # Top triangle
    for i in range(int((n/2))):
        pattern = ('.|.'*(2*i+1))
        print(pattern.center(m, '-'))
    # Welcome
    pattern2 = 'WELCOME'
    print(pattern2.center(m, '-'))

    # Bottom triangle
    i = int(n/2)
    while i > 0:
        pattern3 = ('.|.'*(2*i-1))
        print(pattern3.center(m, '-'))
        i = i - 1
