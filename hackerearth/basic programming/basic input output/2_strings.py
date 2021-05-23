t = int(input())
for _ in range(t):
    s1, s2 = input().split()
    if len(s1) != len(s2):
        print('NO')
    else:
        d1 = {}
        d2 = {}
        flag = True
        for i in range(len(s1)):
            if s1[i] in d1.keys():
                d1[s1[i]] += 1
            else:
                d1[s1[i]] = 1
        for i in range(len(s2)):
            if s2[i] in d2.keys():
                d2[s2[i]] += 1
            else:
                d2[s2[i]] = 1
        # print('d1: ', d1)
        # print('d2: ', d2)
        # print('flag: ', flag)
        for i in d1.keys():
            if i not in d2.keys():
                print('NO')
                flag = False
                break
            else:
                if d1[i] != d2[i]:
                    print('NO')
                    flag = False
                    break
                del d2[i]
            # print('d1: ', d1)
            # print('d2: ', d2)
            # print('flag: ', flag)
        if not d2 or flag:
            print('YES')
        elif d2 and flag:
            print('NO')
