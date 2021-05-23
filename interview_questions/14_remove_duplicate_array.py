def remove_dup(arr, n):
    ls = []
    for i in range(0, n-1):
        if arr[i] == arr[i+1]:
            continue
        else:
            ls.append(arr[i])
    print(ls)

arr = [1,1,2,2,2,3,4,4,4,5,5]
print(list(set(arr)))
remove_dup(arr, len(arr))
