def rain_water(arr, n):
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = arr[0]
    max = arr[0]
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
            left_max[i] = max
        else:
            left_max[i] = max
    max = arr[-1]
    for i in reversed(range(n)):
        if arr[i] > max:
            max = arr[i]
            right_max[i] = max
        else:
            right_max[i] = max

    water = 0
    for i in range(n):
        water += min(right_max[i], left_max[i])-arr[i]
    print(water)

arr = [1,0,2,0,1,0,3,1,0,2]
rain_water(arr, len(arr))
