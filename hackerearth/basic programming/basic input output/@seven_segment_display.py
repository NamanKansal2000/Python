t = int(input())
for _ in range(t):
    n = input()
    count = 0
    num_match = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    for i in n:
        count += num_match[int(i)]
    s = ''
    if count%2 == 0:
        s = '1'*(count//2)
    else:
        s = '7'
        s += '1'*((count-3)//2)
    print(s)
