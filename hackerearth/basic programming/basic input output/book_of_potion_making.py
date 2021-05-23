s = input()
if len(s)<10:
    print('Illegal ISBN')
else:
    num = 0
    count = 1
    for i in s:
        num+=count*int(i)
        count+=1
    if num%11 == 0:
        print('Legal ISBN')
    else:
        print('Illegal ISBN')
