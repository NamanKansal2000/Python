fname = input('Enter the file name: ')
fhand = open(fname)

counts = dict()

for line in fhand:
    words = line.split()  # list of splitted words
    for word in words:
        counts[word] = counts.get(word, 0)+1  # Dct of words list

# Find the most frequent letters
bigword = None
bigcount = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
