def spiralOrder(A):
    m = len(A)
    # print(m)
    n = len(A[0])
    left, right = 0, n-1
    top, bottom = 0,  m-1
    row, col = 0, 0
    direction = 0
    s = []
    while (right >= left) and (bottom >= top):
        if (direction == 0):
            for col in range(left, right+1):  # right
                s.append(A[row][col])
            top += 1

        elif (direction == 1):
            for row in range(top, bottom+1):  # bottom
                s.append(A[row][col])
            right -= 1
        elif direction == 2:
            for col in reversed(range(left, right+1)):  # left
                s.append(A[row][col])
            bottom -= 1
        else:
            for row in reversed(range(top, bottom+1)):  # top
                s.append(A[row][col])
            left += 1
        direction = (direction+1) % 4
    return s


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

s = spiralOrder(A)
print(s)
