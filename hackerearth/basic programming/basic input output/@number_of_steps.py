n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = float('inf')
for i in a:
    if i < m:
        m = i
count = 0
flag = True
while flag:
    flag = False
    for i in range(n):
        while a[i] > m and a[i]!=0:
            a[i] = a[i] - b[i]
            count+=1
            flag = True
        if m > a[i]:
            m = a[i]
        if m < 0:
            break
if m < 0:
    print(-1)
else:
    print(count)
