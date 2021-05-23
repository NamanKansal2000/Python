def common(l1,l2):
    dict = {}
    common = []
    for i in l1:
        if i not in dict:
            dict[i] = [1,0]
        else:
            dict[i][0]+=1
    for i in l2:
        if i in dict:
            dict[i][1] +=1
    for i in dict:
        if dict[i][1]>0:
            common.append(min(dict[i])*[i])
    print(dict)
    print(common)

common([1,1,3,2,1,3,4,1,2], [1,4,3,5,6,3])
