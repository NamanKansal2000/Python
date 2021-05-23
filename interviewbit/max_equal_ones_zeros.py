def findMaxLength(nums):
    max_equal = 0
    start, stop = 0, 1
    curr = 0
    sum = 0
    flag = 0
    for i in range(len(nums)):
        sum += 1 if nums[i] == 1 else -1
        if sum == 0:
            flag = 1
            start = curr
            stop = i
            continue
    if flag == 0:
        print('No such array exist')
        return None
    max_equal = len(nums[start:stop])
    print('Index:- [{},{}]'.format(start, stop))
    return max_equal


print(findMaxLength([0, 0, 1, 1, 0, 0, 1, 1]))
