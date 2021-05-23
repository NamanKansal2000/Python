def findSubString(s, t):
    d = {}
    for c in t:
        d[c] = d.get(c, 0) + 1
    print(d)
    i, j = 0, 0
    matched = 0
    start, size = -1, 0
    while i < len(s):
        while matched == len(t):
            c = s[j]
            if c in d:
                count = d[c]
                if count == 0:
                    matched -= 1
                d[c] = count + 1
            j += 1

        c = s[i]
        if c in d:
            count = d[c]
            d[c] = count - 1

            if count > 0:
                matched += 1
                if matched == len(t):
                    while s[j] not in d or d[s[j]] < 0:
                        if s[j] in d:
                            d[s[j]] += 1
                        j += 1

                    new_size = i - j + 1
                    if start == -1 or size > new_size:
                        start, size = j, new_size

        i += 1

    return s[start:start + size] if start != -1 else ''


string = "thisisateststring"
pat = "tist"
print(string)
print(pat)
# print("Smallest window is : ")
print(findSubString(string, pat))
