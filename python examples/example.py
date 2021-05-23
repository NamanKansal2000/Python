def check_list(li, i):
    if (i == len(li)-1):
        print('if1 True', i)
        return True
    isarranged = check_list(li, i+1)
    print(l)
    print(i)
    print('issarranged: ', isarranged)
    if (isarranged == True):
        print(li[i], i)
        return li[i] <= li[1+i]
    else:
        return False

l = [1,2,3,4,5]
result = check_list(l, 0)
if result == True:
    print('Yes')
else:
    print('No')
