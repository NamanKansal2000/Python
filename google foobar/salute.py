def solution(s):
    l = list(s)
    count = 0
    right, left = [], []
    right = [i for i, x in enumerate(s) if x == ">"]
    left = [i for i, x in enumerate(s) if x == "<"]
    # print(right, left)
    for i in right:
        for j in left:
            if i < j:
                count += 2
    return(count)


# def solution(str):
#     n = len(str)
#     i = 0
#     count = 0
#     while(i < n):
#         r = str.find('>', i, n)
#         if r == -1:
#             break
#         j = r+1
#         while(j < n):
#             s = str.find('<', j, n)
#             if s == -1:
#                 break
#             count += 2
#             j = s+1
#         i = r+1
#     return count


# str = input('Enter string: ')

# print(solution(str))

print(solution('<<>><'))
