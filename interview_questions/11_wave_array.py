def wave(arr,n):
    for i in range(0, n, 2):
        if arr[i-1] > arr[i] and i > 0:
            arr[i-1], arr[i] = arr[i], arr[i-1]
        if i < n-1 and arr[i+1] > arr[i]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
    print(arr)

arr = [1,2,3,4,5,6,7,8,9,10]
wave(arr, len(arr))
