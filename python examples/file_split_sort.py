fname = input('Enter the file name: ')
fhand = open(fname)
sword = list()
for line in fhand:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print(words)

    for word in words:
        if word in sword:
            continue
            #print(sword)
        else:
            sword.append(word)
sword.sort()
print(sword)
