def longest_substring(s):
    anchor = 0
    curr, maxx = 0, float('-inf') # change this to max constrint limit of s in problem
    start, end = 0, 0
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = d.get(s[i],0)+1
            # print(d)
        else:
            curr = i-anchor
            if curr > maxx:
                start = anchor
                end = i
                maxx = curr
            anchor = i
            # print('--------')
            del d
            d = {}
            d[s[i]] = 1
            # print(d)
            # print(i, s[i])
    str = s[start:end]
    return str, len(str)

s = 'HSBHAKSOAOJJCOJSMOQKCSPSSSSL'
print(longest_substring(s))
