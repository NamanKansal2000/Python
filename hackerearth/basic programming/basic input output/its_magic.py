
n = int(input())
arr = list(map(int,input().split()))
sum_a = sum(arr)
# print(sum_a)

min = float('inf')
index = 0
val = sum_a%7
# print(val)
for i in range(len(arr)):
    # print(arr[i]%7, end=' ')
    if arr[i]%7 == val:
        if arr[i] < min:
            min = arr[i]
            index = i
            # print('min: ', min, 'i: ', index)
# print()
if min != float('inf'):
    print(index)
else:
    print(-1)
