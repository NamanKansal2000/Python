fname = input('Enter the file name: ')
fhand = open(fname)
counts = dict()
email = list()
for line in fhand:
    #line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    #print('Words: ',words)
    email.append(words[1])
for word in email:
    counts[word] = counts.get(word,0) + 1

bigword = None
bigcount = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword , bigcount)
