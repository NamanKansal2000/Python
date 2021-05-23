fname = input('Enter the file name: ')
fhand = open(fname)

counts = dict()

for line in fhand:
    words = line.split('/')[2]  # list of splitted words
    counts[words] = counts.get(words, 0)+1  # Dct of words list

print(counts)

fhand.close()
