def max_sum_subarray(arr, n):
    start = end = poi = 0
    max = arr[0]
    curr = 0
    for i in range(n):
        curr += arr[i]
        if max < curr:
            max = curr
            start = poi
            end = i

        if curr < 0:
            curr = 0
            poi = i+1
    print('max sum: ', max)
    print('location: ',(start, end))
    print('array', arr[start: end+1])

arr = [4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
arr = [-1,-1,-1]
max_sum_subarray(arr,len(arr))
