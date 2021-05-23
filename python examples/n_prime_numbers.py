def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = int(input())
c, counter = 1,0
while True:
    c+=1
    if isprime(c):
        if counter == n:
            break
        else:
            counter+=1
            print(c, end = ' ')
