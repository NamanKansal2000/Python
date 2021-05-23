def min_diff(arr, n):
    arr.sort()
    diff = float('inf')
    for i in range(n-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]
    print(diff)

arr = [2,3,5,1,7,10,4]
min_diff(arr, len(arr))
