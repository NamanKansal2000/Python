from fractions import Fraction


def make_fraction(mat):
    k = []
    for i in range(len(mat)):
        k.append([])
        for j in range(len(mat[i])):
            k[i].append(Fraction(mat[i][j].numerator, mat[i][j].denominator))
    return k


def gauss_elmination(m, values):
    mat = make_fraction(m)
    for i in range(len(mat)):
        index = -1
        for j in range(i, len(mat)):
            if mat[j][i].numerator != 0:
                index = j
                break
        # if index == -1:
        #     raise ValueError('Gauss elimination failed!')
        mat[i], mat[index] = mat[index], mat[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i+1, len(mat)):
            if mat[j][i].numerator == 0:
                continue
            ratio = -mat[j][i]/mat[i][i]
            for k in range(i, len(mat)):
                mat[j][k] += ratio * mat[i][k]
            values[j] += ratio * values[i]
    res = [0 for i in range(len(mat))]
    for i in range(len(mat)):
        index = len(mat) - 1 - i
        end = len(mat) - 1
        while end > index:
            values[index] -= mat[index][end] * res[end]
            end -= 1
        res[index] = values[index]/mat[index][index]
    return res


def inverse(mat):
    fmat = transpose(mat)
    mat_inv = []
    for i in range(len(fmat)):
        values = [Fraction(int(i == j), 1) for j in range(len(mat))]
        mat_inv.append(gauss_elmination(fmat, values))
    return mat_inv


def transpose(mat):
    fmat = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            fmat[j][i] = (mat[i][j])
    return fmat


def mul(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            res[i].append(Fraction(0, 1))
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res


def split_to_QR(mat, r_len):
    q_len = len(mat) - r_len
    Q = []
    R = []
    for i in range(q_len):
        # for j in range(q_len):
        #     if i == j:
        #         Q.append(1 - mat[i][j])
        #     else:
        #         Q.append(-mat[i][j])
        Q.append([int(i == j)-mat[i][j] for j in range(q_len)])
        R.append(mat[i][q_len:])
        # print(R)
    return Q, R


# def show(mat):
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             print(mat[i][j], end=" "*10)
#         print()
#     print()


def simplify(x, y):
    d = gcd(x, y)
    x = int(x/d)
    y = int(y/d)
    return Fraction(x, y)


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def LCMofArray(a):
    lcm = a[0]
    for i in range(1, len(a)):
        lcm = int(lcm*a[i]/gcd(lcm, a[i]))
    return lcm


def transition(mat):
    sum_list = list(map(sum, mat))
    bool_val = list(map(lambda x: x == 0, sum_list))
    index = set([i for i, x in enumerate(bool_val) if x])
    new_mat = []
    for i in range(len(mat)):
        new_mat.append(list(map(lambda x: Fraction(0, 1) if(
            sum_list[i] == 0) else simplify(x, sum_list[i]), mat[i])))
    transition_mat = []
    zeros_mat = []
    for i in range(len(new_mat)):
        if i not in index:
            transition_mat.append(new_mat[i])
        else:
            zeros_mat.append(new_mat[i])
    my_extend(transition_mat, zeros_mat)
    fmat = []
    for i in range(len(transition_mat)):
        fmat.append([])
        extend_mat = []
        for j in range(len(transition_mat)):
            if j not in index:
                fmat[i].append(transition_mat[i][j])
            else:
                extend_mat.append(transition_mat[i][j])
        my_extend(fmat[i], extend_mat)
    return [fmat, len(zeros_mat)]


def my_extend(mat1, mat2):
    for i in range(len(mat2)):
        mat1.append(mat2[i])


def solution(mat):
    fmat, length = transition(mat)
    # print('transition:')
    # show(fmat)
    # print()
    if length == len(mat):
        return [1, 1]
    Q, R = split_to_QR(fmat, length)
    # print('Q')
    # show(Q)
    # print()
    # print('R:')
    # show(R)
    # print()
    F = inverse(Q)
    # print('F:-')
    # show(F)
    # print()
    FR = mul(F, R)
    # print('FR:-')
    # show(FR)
    row = FR[0]
    l = [i.denominator for i in row]
    lcm = LCMofArray(l)
    # print(lcm)
    ans = list(map(lambda x: int(x.numerator * lcm/x.denominator), row))
    ans.append(lcm)
    return ans


mat = [
    [0, 1, 0, 0, 0, 1],  # s0, the initial state, goes to s1 and s5 with equal probability
    [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4, but with different probabilities
    [0, 0, 0, 0, 0, 0],  # s2 is terminal, and unreachable (never observed in practice)
    [0, 0, 0, 0, 0, 0],  # s3 is terminal
    [0, 0, 0, 0, 0, 0],  # s4 is terminal
    [0, 0, 0, 0, 0, 0],  # s5 is terminal
]
mat = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
mat = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
mat = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
mat = [
    [1, 2, 3, 0, 0, 0],
    [4, 5, 6, 0, 0, 0],
    [7, 8, 9, 1, 0, 0],
    [0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
mat = [[0]]
mat = [
    [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
    [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
    [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
    [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

mat = [
    [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
    [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
    [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
    [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
    [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
mat = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
mat = [
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
mat = [
    [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
    [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
    [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
mat = [
    [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
    [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
    [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
    [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
print(solution(mat))
