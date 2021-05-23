# You are in an infinite 2D grid where you can move in any of the 8 directions
#:
#
#  (x,y) to
#     (x+1, y),
#     (x - 1, y),
#     (x, y+1),
#     (x, y-1),
#     (x-1, y-1),
#     (x+1,y+1),
#     (x-1,y+1),
#     (x+1,y-1)
# You are given a sequence of points and the order in which you need to cover
# the points. Give the minimum number of steps in which you can achieve it.
# You start from the first point.
# Input : [(0, 0), (1, 1), (1, 2)]
# Output : 2


def min_steps(A, B):
    count = 0
    for i in range(len(A)):
        count += max(abs(A[i+1] - A[i]), abs(B[i+1] - B[i]))
    return count
