def isprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
            return False
    return True

def r(ls, n):
    # print(ls)
    for i in range(len(ls)-1):
        if n <= ls[0]:
            return chr(ls[0])
        if n >= ls[-1]:
            return chr(ls[-1])
        if ls[i] <= n and ls[i+1] > n:
            # print('i: ', ls[i])
            # print('i+1: ', ls[i+1])
            if abs(n-ls[i]) <= abs(ls[i+1]-n):
                return chr(ls[i])
            else:
                return chr(ls[i+1])


ls = []
for i in range(ord('A'), ord('Z')+1):
    if isprime(i):
        ls.append(i)
for i in range(ord('a'), ord('z')+1):
    if isprime(i):
        ls.append(i)
# print(ls)
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    # print(s)
    for i in range(n):
        # print(ord(s[i]))
        s[i] = r(ls, ord(s[i]))
    # print(s)
    print(''.join(s))
