def sum_missing_num(arr):
    sum = 0
    for i in arr:
        sum += i
    n = arr[-1]
    actual_sum = int((n * (n+1)) / 2)
    missing_num = actual_sum - sum
    print(missing_num)

def xor_missing_num(arr):
    xor = 0
    actual_xor = 0
    for i in arr:
        xor ^= i
    for j in range(1, arr[-1]+1):
        actual_xor ^= j
    missing_num = actual_xor ^ xor
    print(missing_num)


arr = [1,2,3,4,6,7,8]
sum_missing_num(arr)
xor_missing_num(arr)
