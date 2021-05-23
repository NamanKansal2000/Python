# ek baar code ko run karke dekho maine kuch print statements include ki hai taaki
# samjh aa jaaye ki konsa operation kahan ho raha hai


# to convert each one in map to 0
def solution(map):
    flag = 0
    min_dist = []
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if map[i][j] == 1:
                flag = 1
                map[i][j] = 0
                print('new map:- ')
                print('changed (i, j):- ', (i, j))
                show(map)
                print()
                min_dist.append(sol(map))
                map[i][j] = 1
                print('min_dist:- ', min_dist)
                print()
    if flag == 1:
        return min(min_dist)
    else:
        return sol(map)


def sol(map):
    x = len(map)  # final dest x
    y = len(map[0])  # final dest y
    i = 0  # initial x
    j = 0  # initial y
    visited = [[0 for a in range(y)] for b in range(x)]  # to track the points visited
    min_dist = shortest_path(map, visited, i, j, x-1, y-1,
                             float('inf'), 0)  # call the shortest path
    return min_dist


def isValid(map, visited, x, y):
    # it checks if our new coordinates our within the range (0, h-1) and (0, w-1)
    if (len(map) > x >= 0 and len(map[0]) > y >= 0):
        return True


def isSafe(map, visited, x, y):
    # this checks if the new cordinates corresponds to a 0 in map and also it is not
    # a visited location
    return not(map[x][y] == 1 or visited[x][y] == 1)


def shortest_path(map, visited, i, j, x, y, min_dist, dist):
    # base condition of our recursion loop that it ends when it reaches destination co-ordinates
    if i == x and j == y:
        return min(min_dist, dist)

    # change the visited value as 1 when we reach that location
    # this track that we are not visiting same location twice
    # as we have checked this condition in isSafe() fxn
    visited[i][j] = 1
    print()
    print('visited:- ')
    show(visited)
    print()

    # this checks for all 4 direction

    # left
    if isValid(map, visited, i+1, j) and isSafe(map, visited, i+1, j):
        min_dist = shortest_path(map, visited, i+1, j, x, y, min_dist, dist + 1)

    # right
    if isValid(map, visited, i-1, j) and isSafe(map, visited, i-1, j):
        min_dist = shortest_path(map, visited, i-1, j, x, y, min_dist, dist + 1)

    #  bottom
    if isValid(map, visited, i, j+1) and isSafe(map, visited, i, j+1):
        min_dist = shortest_path(map, visited, i, j+1, x, y, min_dist, dist + 1)

    # top
    if isValid(map, visited, i, j-1) and isSafe(map, visited, i, j-1):
        min_dist = shortest_path(map, visited, i, j-1, x, y, min_dist, dist + 1)

    # this condition runs if there is no further way to go
    # meaning no possible path is there
    # it will then assign the current coordinates of i and j to 0
    # basically it backtracks its way

    visited[i][j] = 0
    print('Code backtracked')
    print()
    return min_dist


def show(map):
    for i in map:
        col = []
        for j in i:
            col.append(j)
        print(col)


# map = [[0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
#        [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# map1 = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# map2 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# map3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
map = [[0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0]]
# map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
#       [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
map = [[0, 0]]
print(solution(map))
