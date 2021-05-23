def count(x1, x2, y1, y2):

    ans = 0
    delx = abs(x1-x2)
    dely = abs(y1-y2)

    if delx == 1 and dely == 0 or delx == 0 and dely == 1:
        ans += 3
    elif delx == 1 and dely == 1:
        ans += 2
    elif delx == 2 and dely == 0 or delx == 0 and dely == 2:
        ans += 2
    elif delx == 2 and dely == 1 or delx == 1 and dely == 2:
        ans += 1
    elif delx == 2 and dely == 2:
        ans += 4
    else:
        if x1 >= x2 and y1 <= y2:  # quadrant 1
            if count(x1-1, x2, y1+2, y2) > count(x1-2, x2, y1+1, y2):
                x1 = x1-2
                y1 = y1+1
            else:
                x1 = x1-1
                y1 = y1+2

        elif x1 >= x2 and y1 >= y2:  # quadrant 2
            if count(x1-1, x2, y1-2, y2) > count(x1-2, x2, y1-1, y2):
                x1 = x1-2
                y1 = y1-1
            else:
                x1 = x1-1
                y1 = y1-2

        elif x1 <= x2 and y1 >= y2:  # quadrant 3
            if count(x1+1, x2, y1-2, y2) > count(x1+2, x2, y1-1, y2):
                x1 = x1+2
                y1 = y1-1
            else:
                x1 = x1+1
                y1 = y1-2

        elif x1 <= x2 and y1 <= y2:  # quadrant 4
            if count(x1+1, x2, y1+2, y2) > count(x1+2, x2, y1+1, y2):
                x1 = x1+2
                y1 = y1+1
            else:
                x1 = x1+1
                y1 = y1+2
        ans = 1+count(x1, x2, y1, y2)
    return ans


def solution(src, dest):
    if src == dest:
        return 0
    # coordinate
    x = src % 8
    y = src//8
    tx = dest % 8
    ty = dest//8

    # 4 corner position to diagonal

    return(count(x, tx, y, ty))


print(solution(0, 1))
