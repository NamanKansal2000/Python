def non_repeating(str):
    dict = {}
    for i in str:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for i in range(len(str)):
        if dict[str[i]] == 1:
            print((str[i], i))

str = 'Naman'
non_repeating(str.lower())
