def shortest_path(x, y, map):
    w = len(map[0])
    h = len(map)
    visited = [[None for i in range(w)] for i in range(h)]
    visited[x][y] = 1

    ls = [(x, y)]
    while ls:
        x, y = ls.pop(0)
        #print(x, y)
        for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            nx, ny = x + i[0], y + i[1]
            if h > nx >= 0 and w > ny >= 0:
                if visited[nx][ny] is None:
                    visited[nx][ny] = visited[x][y] + 1
                    # print(visited)
                    if map[nx][ny] == 1:
                        continue
                    ls.append((nx, ny))
                    # print(ls)

    return visited


def solution(map):
    w = len(map[0])
    h = len(map)
    tb = shortest_path(0, 0, map)
    bt = shortest_path(h-1, w-1, map)
    visited = []
    print(tb)
    print(bt)
    min_dist = 2 ** 32-1
    for i in range(h):
        for j in range(w):
            #print('tb:- ', tb[i][j])
            #print('bt', bt[i][j])
            # if tb[i][j] and bt[i][j]:
            min_dist = min(tb[i][j] + bt[i][j] - 1, min_dist)
            #print('min_dist:- ', min_dist)
    return min_dist


map = [[0, 0]]  # solution 11
print(solution(map))
