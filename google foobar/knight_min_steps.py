dp = [[0 for i in range(8)] for j in range(8)]  # initializing the matrix.


def count(x, y, tx, ty):
    if (x == tx and y == ty):
        return dp[0][0]

    elif(dp[abs(x - tx)][abs(y - ty)] != 0):
        return dp[abs(x - tx)][abs(y - ty)]
    else:

        x1, y1, x2, y2 = 0, 0, 0, 0
        if (x <= tx):
            # 1st quadrant
            if (y <= ty):
                x1 = x + 2
                y1 = y + 1
                x2 = x + 1
                y2 = y + 2
            # 4th quadrant
            else:
                x1 = x + 2
                y1 = y - 1
                x2 = x + 1
                y2 = y - 2
        else:
            # 2nd quadrant
            if (y <= ty):
                x1 = x - 2
                y1 = y + 1
                x2 = x - 1
                y2 = y + 2
            # 3rd quadrant
            else:
                x1 = x - 2
                y1 = y - 1
                x2 = x - 1
                y2 = y - 2
        dp[abs(x - tx)][abs(y - ty)] = min(count(x1, y1, tx, ty), count(x2, y2, tx, ty)) + 1
        dp[abs(y - ty)][abs(x - tx)] = dp[abs(x - tx)][abs(y - ty)]
        return dp[abs(x - tx)][abs(y - ty)]


# Driver Code
def solution(src, dest):

    # size n*n
    n = 8

    # convert to co-ordinate
    # (x, y) src coordinate.
    # (tx, ty) dest coordinate.
    x = src % 8
    y = src//8
    tx = dest % 8
    ty = dest//8
    # 4 corner position to diagonal
    if ((x == 1 and y == 1 and tx == 2 and ty == 2) or
            (x == 2 and y == 2 and tx == 1 and ty == 1)):
        ans = 4
    elif ((x == 1 and y == n and tx == 2 and ty == n - 1) or
          (x == 2 and y == n - 1 and tx == 1 and ty == n)):
        ans = 4
    elif ((x == n and y == 1 and tx == n - 1 and ty == 2) or
          (x == n - 1 and y == 2 and tx == n and ty == 1)):
        ans = 4
    elif ((x == n and y == n and tx == n - 1 and ty == n - 1)
          or (x == n - 1 and y == n - 1 and tx == n and ty == n)):
        ans = 4
    else:
        dp[1][0] = 3  # adjacent in x direction
        dp[0][1] = 3  # adjacent in y direction
        dp[1][1] = 2  # immediate diagonally opposite except corners
        dp[2][0] = 2  # adjacent 2nd in x
        dp[0][2] = 2  # adjacent 2nd in y
        dp[2][1] = 1  # normal 1 move only if move is valid
        dp[1][2] = 1  # normal 1 move only if move is valid

        ans = count(x, y, tx, ty)

    return(ans)


print(solution(19, 36))
