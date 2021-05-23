def merge(arr):
    arr.sort(key= lambda x:x[0])
    ls = []
    ls.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i][0] <= ls[-1][1]:
            ls[-1][1] = max(ls[-1][1], arr[i][1])
        else:
            ls.append(arr[i])
    return ls

arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
print(merge(arr))

intervals = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
inter = list(map(list,intervals))
# for i in range(len(intervals)):
#     inter.append(list(intervals[i]))
print(inter)
