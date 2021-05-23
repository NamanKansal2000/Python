def subarray_sum(arr, n ,sum):
    start = 0
    curr_sum = arr[0]
    i = 1
    count = 0
    while i <= n:
        while curr_sum > sum:
            curr_sum -= arr[start]
            start +=1

        if curr_sum == sum:
            count += 1
            print("Subarray ", count)
            print("Subarray indices: ", start, i-1)
            print("Subarray : ", arr[start:i])
            print()
        if i < n:
            curr_sum += arr[i]
        i += 1



arr = [15, 2, 4, 8, 9, 5, 10, 23]
arr = [0,1]
subarray_sum(arr, len(arr), 1)
