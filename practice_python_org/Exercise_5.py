import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []

ls = [common.append(i) for i in a for j in b if i == j if i not in common]
print(common)

# generate no of elements using random fxn

a = random.randint(0, 10)
b = random.randint(0, 10)

rlist_1 = [random.randint(0, 100) for i in range(a)]
rlist_2 = [random.randint(0, 100) for i in range(b)]
print('List1: ', rlist_1, '\nList2: ', rlist_2)
c = []  # list that stores common elements

ls = [c.append(i) for i in rlist_1 for j in rlist_2 if i == j if i not in c]
if c == []:
    print("No common elements in these two list")
else:
    c.sort()
    print(c)
