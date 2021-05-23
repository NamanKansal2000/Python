def right_matrix_rotate(arr):
    top = 0
    bottom = len(arr)-1
    left = 0
    right = len(arr[0])-1

    while left < right and top < bottom:
        prev = arr[top+1][left]
        for i in range(left, right+1):
            curr = arr[top][i]
            arr[top][i] = prev
            prev = curr
        top+=1

        for i in range(top, bottom+1):
            curr = arr[i][right]
            arr[i][right] = prev
            prev = curr
        right -= 1

        for i in range(right, left-1, -1):
            curr = arr[bottom][i]
            arr[bottom][i] = prev
            prev = curr
        bottom -= 1

        for i in range(bottom, top-1, -1):
            curr = arr[i][left]
            arr[i][left] = prev
            prev = curr
        left += 1
    for i in range(len(arr)):
        print(arr[i])

arr = [
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ]
        ]
right_matrix_rotate(arr)
