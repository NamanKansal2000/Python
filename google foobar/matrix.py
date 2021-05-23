from fractions import Fraction


def transpose(mat):
    fmat = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            fmat[j][i] = (mat[i][j])
    return fmat


def mul(mat1, mat2):
    c = []
    for i in range(len(mat1)):
        c.append([])
        for j in range(len(mat2)):
            c[i].append(0)
            for k in range(len(mat1[0])):
                c[i][j] += (mat1[i][k]) * (mat2[k][j])
    return c


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixDeternminant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant


def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1] / determinant, -1*m[0][1] / determinant],
                [-1*m[1][0] / determinant, m[0][0]/determinant]]

    find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


mat = [
    [0, 1, 0, 0, 0, 1],  # s0, the initial state, goes to s1 and s5 with equal probability
    [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4, but with different probabilities
    [0, 0, 0, 0, 0, 0],  # s2 is terminal, and unreachable (never observed in practice)
    [0, 0, 0, 0, 0, 0],  # s3 is terminal
    [0, 0, 0, 0, 0, 0],  # s4 is terminal
    [0, 0, 0, 0, 0, 0],  # s5 is terminal
]

mat1 = [[1, 0], [-2/3, 1]]
mat2 = [[1, 3, 5], [2, 4, 7], [9, 5, 1]]
print('mat', mat)
print('transpose', transpose(mat))
print('mul', mul(mat1, mat1))
print('inv', getMatrixInverse(mat1))
print('inv', getMatrixInverse(mat2))
