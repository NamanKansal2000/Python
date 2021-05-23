fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        continue
    words = line.split()
    count = count + 1
    print(words[1])
print("There were", count, "lines in the file with From as the first word")
