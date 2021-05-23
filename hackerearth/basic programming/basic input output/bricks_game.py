n = int(input())
i = 1
while n!=0:
    n -= i
    if n < 1:
        print('Patlu')
        break
    n -= 2*i
    if n < 1:
        print('Motu')
        break
    i+=1
