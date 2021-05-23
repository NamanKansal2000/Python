def left(str):
    a = str[1:]
    return a+str[0]

def right(str):
    a = str[:-1]
    return str[-1]+a

arr = [-1,2,2,-4]


# here negative means left rotation
# positive means right
str = 'naman'
sum = sum(arr)
if sum < 0:
    for j in range(abs(sum)):
        str = left(str)
        print('left: ', str)
if sum > 0:
    for j in range(sum):
        str = right(str)
        print('right: ', str)
