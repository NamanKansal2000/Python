map = [[0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# map1 = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# map2 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# map3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
map = [[0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0]]


def solution(map):
    flag = 0
    min_dist = []
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if map[i][j] == 1:
                map[i][j] = 0
                flag = 1
                print(map)
                min_dist.append(sol(map))
                print('min_dist:-', min_dist)
                print('i:-', i, ' j:-', j)
                map[i][j] = 1
                print(map[i][j])
                print(map)
                print()
    if flag == 1:
        return min(min_dist)
    else:
        return sol(map)


def sol(map):
    store = []
    h = len(map)
    w = len(map[0])
    flag = 0
    countones = 0
    addof1 = list()

    # finalans=0

    for i in range(0, h):
        for j in range(0, w):
            if map[i][j] == 1:
                countones += 1
                addof1.append((i, j))

    ans = 0

    def isvalid(x, y, a, b):
        if x == h-1 and y == w-1:
            return False
        elif h > a >= 0 and w > b >= 0:
            if map[a][b] == 0:
                return True
        else:
            return False

    prev = ()

    def findpath(x, y, prevx, prevy, map):
        nonlocal ans
        nonlocal flag
        # nonlocal finalans
        xx = x
        yy = y
        prev = (prevx, prevy)
        l = list()
        lmin = list()
        stored = 0
        if len(store) != 0:
            for tup in store:
                if tup[0] == x and tup[1] == y:
                    stored = 1
                    return tup[2]
        if stored == 0:
            if (x, y) == (h-1, w-1):
                # print('if worked')
                # nonlocal x
                # nonlocal y
                x = h-1
                y = w-1
                # print('flag =',flag)
                if flag == 0:
                    ans += 1
                # print('ans =',ans)
                # print('x,y =',x,y)
                # print('Reached goal')
                flag = 0
                finalans = ans
                # print(ans)
                flag = 1
                return finalans
                # exit()
                # return ans
                # return retans(ans)
                # return True,ans
            # elif not x>=0 and x<h and y>=0 and y<w:
            #    return 100
                # return False,ans
            # elif map[x][y]==1:
                # return False,ans
            #    return 100
            elif (x, y) != (h-1, w-1) and flag != 1:
                # print('elif worked')
                # print('else: ',x,y)
                count = 0
                if isvalid(x, y, x+1, y):
                    # if (x+1,y)==(h-1,y-1):
                    #    #print(x+1,y)
                    #    #print('Reached goal')
                    #    #print(ans)
                    # exit()
                    #    return ans
                    if not (x+1, y) == (prevx, prevy):
                        # print('case 1',x,y,x+1,y)
                        count += 1
                        # print('initial ans =',ans)
                        # print('flag =',flag)
                        if flag == 0:
                            ans += 1
                        # print('final ans =',ans)
                        # return findpath(x+1,y,x,y)
                        lmin.append(findpath(x+1, y, x, y, map))
                if isvalid(x, y, x, y+1):
                    # if (x,y+1)==(h-1,y-1):
                    #    #print(x,y+1)
                    #    #print('Reached goal')
                    #    #print(ans)
                    # exit()
                    #    return ans
                    if not (x, y+1) == (prevx, prevy):
                        # print('case 2',x,y,x,y+1)
                        count += 1
                        # print('initial ans =',ans)
                        # print('flag =',flag)
                        if flag == 0:
                            ans += 1
                        # print('final ans =',ans)
                        # return findpath(x,y+1,x,y)
                        lmin.append(findpath(x, y+1, x, y, map))
                if isvalid(x, y, x-1, y):
                    # if (x-1,y)==(h-1,y-1):
                    #    #print(x-1,y)
                    #    #print('Reached goal')
                    #    #print(ans)
                    # exit()
                    #    return ans
                    if not (x-1, y) == (prevx, prevy):
                        # print('case 3',x,y,x-1,y)
                        count += 1
                        # print('initial ans =',ans)
                        # print('flag =',flag)
                        if flag == 0:
                            ans += 1
                        # print('final ans =',ans)
                        # return findpath(x-1,y,x,y)
                        lmin.append(findpath(x-1, y, x, y, map))
                if isvalid(x, y, x, y-1):
                    # if (x,y-1)==(h-1,y-1):
                    #    #print(x,y-1)
                    #    #print('Reached goal')
                    #    #print(ans)
                    # exit()
                    #    return ans
                    if not (x, y-1) == (prevx, prevy):
                        # print('case 4',x,y,x,y-1)
                        count += 1
                        # print('initial ans =',ans)
                        # print('flag =',flag)
                        if flag == 0:
                            ans += 1
                        # print('final ans =',ans)
                        # return findpath(x,y-1,x,y)
                        lmin.append(findpath(x, y-1, x, y, map))
                if count == 0:
                    return 100
                    # return False,ans
            try:
                # ans=1+min(lmin)
                ans = min(lmin)
            except:
                flag = flag
                # print('exception since list was empty')
            # store.append([xx,yy,findpath(xx,yy,prevx,prevy,map)])
            store.append([x, y, ans])
            return ans
    return findpath(0, 0, 0, -1, map)


# sol(map)
    # return finalans


# print(solution(map))
# print(solution(map1))
lll = []
maps = list()
h = len(map)
w = len(map[0])
row = []


def show(map):
    for i in map:
        col = []
        for j in i:
            col.append(j)
        print(col)


# show(map)
print(solution(map))
print('\n')
# show(map1)
# print(solution(map1))
# print('\n')
# show(map2)
# print(solution(map2))
# print('\n')
# show(map3)
# print(solution(map3))
print('\n\nAlll arrrreeeeee correeccttttttt!!!!!!!')
# l=list()
# for i in range(0,h):
#    for j in range(0,w):
#        if map[i][j]==1:
#            t=(i,j)
#            l.append(t)
# count=len(l)
# print(count)
# for items in l:
#    print(items[0],items[1])
# maps=[]
# for i in range(0,count):
#    map[l[i][0]][l[i][1]]=0
# print(map)
#    maps.append(map)
# print(solution(map))
#    map[l[i][0]][l[i][1]]=1

# for mappp in maps:
#    print('solution:')
#    print(solution(mappp))
# for mapp in maps:
#    print(solution(mapp))

# print(findpath(0,0,0,-1,mapp))
# lll.append(findpath(0,0,0,-1,mapp))
# i+=1

# mapp=[[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# print(solution(map1))
# print(solution(mapp))
# print(findpath(0,0,0,-1,map1))
# print(findpath(0,0,0,-1,mapp))
# print(lll)
