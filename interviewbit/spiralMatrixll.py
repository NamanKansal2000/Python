def generateMatrix(A):
    s = []
    B = [[0 for i in range(A)]for j in range(A)]
    c = 1
    for i in range(A):
        for j in range(A):
            B[i][j] = c
            c += 1
    print(B)
    left, right = 0, A-1
    top, bottom = 0, A-1
    row, col = 0, 0
    direction = 0
    while(right > left and bottom > top):
        if direction == 0:
            for col in range(left, right):
                s.append(B[row][col])
            top += 1
        if direction == 1:
            for row in range(top, bottom):
                s.append(B[row][col])
            right -= 1
        if direction == 2:
            for col in range(right, left, -1):
                s.append(B[row][col])
            bottom -= 1
        if direction == 3:
            for row in range(bottom, top, -1):
                s.append(B[row][col])
            left += 1
        direction = (direction+1) % 4
    return s


n = int(input("enter value:- "))
print(generateMatrix(n))
