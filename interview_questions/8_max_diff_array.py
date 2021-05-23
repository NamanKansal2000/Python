def max_diff(arr, n):
    min_e = arr[0]
    max_e = arr[0]
    for i in range(1, n):
        if arr[i] < min_e:
            min_e = arr[i]
        if arr[i] > max_e:
            max_e = arr[i]
    max_diff = max_e - min_e
    print(max_diff)

arr = [2,3,5,1,7,10,4]
max_diff(arr, len(arr))
