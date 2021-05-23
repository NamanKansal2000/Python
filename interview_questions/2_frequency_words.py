def frequency_words():
    line = input("Enter the str: ")
    lst = line.split()
    d = {}
    for i in lst:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    print(d)

frequency_words()
