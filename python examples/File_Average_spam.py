fname = input('Enter the file name: ')
fhand = open(fname)
sum = 0
count=0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        rline = line
        count = count + 1
        fval = float(rline[20:])
        #print(rline[20:])
        sum = sum + fval

print('Average Confidence:',sum/count)
