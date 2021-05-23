def partition(n):
    mat = [[0 for i in range(n+1)] for j in range(n+1)]
    mat[0][0] = 1
    for i in range(0, n+1):
        mat[i][0] = 1
    for summand in range(1, n+1):
        for sum in range(1, n+1):
            if summand > sum:
                mat[summand][sum] = mat[summand-1][sum]
            elif summand <= sum:
                inc = mat[summand-1][sum]
                mat[summand][sum] = mat[summand - 1][sum-summand]+inc
    # for i in range(len(mat)):
    #     for j in range(len(mat)):
    #         print(mat[i][j], end=" ")
    #     print()
    return mat[n][n]-1


print(partition(200))

###############################################################################
# This code tells total possible partition
###############################################################################
# def partition(n):
#     mat = [[0 for i in range(n+1)] for j in range(n+1)]
#     mat[0][0] = 1
#     for i in range(0, n+1):
#         mat[i][0] = 1
#     for summand in range(1, n+1):
#         for sum in range(1, n+1):
#             if summand < sum:
#                 mat[summand][sum] = mat[summand-1][sum]
#             elif summand >= sum:
#                 inc = mat[summand-1][sum]
#                 mat[summand][sum] = mat[summand - 1][sum-summand]+inc
#     # for i in range(len(mat)):
#     #     for j in range(len(mat)):
#     #         print(mat[i][j], end=" ")
#     #     print()
#     return mat[n][n]-1
