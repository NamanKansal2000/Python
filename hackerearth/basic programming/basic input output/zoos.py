s = input()

dict = {}
for i in s:
    if i in dict.keys():
        dict[i] +=1
    else:
        dict[i] = 1

if 2* dict['z'] == dict['o']:
    print('Yes')
else:
    print('No')
