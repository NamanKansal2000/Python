def anagrams(s,p):
    P = dict()
    for i in p:
        P[i] = P.get(i,0)+1
    j = 0
    res = []
    S = dict()
    for i in range(len(s)):
        S[s[i]] = S.get(s[i],0)+1
        if i-j == len(p)-1:
            if S == P:
                res.append(j)
            if S[s[j]] == 1:
                del S[s[j]]
            else:
                S[s[j]]-=1
            j+=1

    return res



s = "zccabcccbsbabanabcba"
t = 'abcc'
print(anagrams(s, t))
