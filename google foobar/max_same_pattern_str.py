import math


def solution(s):
    n = len(s)
    l = [i for i in range(1, n+1) if n % i == 0]
    print(l)
    for d in l:
        ss = s[0:d]
        flag = 1
        i = d
        while(i < n):
            if(ss != s[i:i+d]):
                flag = 0
                break
            i += d
        if(flag == 1):
            break
    return int(n/d)


print(solution('abab'))
