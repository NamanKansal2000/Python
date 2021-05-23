def excel(str, n):
    result = 0
    for i in range(n):
        num = ord(str[i])-ord('A')+1
        result += num*pow(26,n-1)
        n -= 1
    print(result)

str = 'ZZz'
excel(str.upper(), len(str))
