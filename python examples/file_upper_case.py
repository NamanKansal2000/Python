# Change all the letters in file to upper case

fname = input('Enter file name: ')
fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)
