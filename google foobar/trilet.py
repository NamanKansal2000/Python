from fractions import Fraction


def solution(mat):
    fmat, length = transition(mat)
    if length == len(mat):
        return [1, 1]
    Q, R = split_to_QR(fmat, length)
    print(Q)
    print(R)


def transition(mat):
    sum_list = list(map(sum, mat))
    bool = list(map(lambda x: False if x else True, sum_list))
    index = [i for i, x in enumerate(sum_list) if x == 0]
    new_mat = []
    for i in range(len(mat)):
        new_mat.append(list(map(lambda x: Fraction(0, 1) if x ==
                                0 else simplify(x, sum_list[i]), mat[i])))
    trans_mat = []
    zeros_mat = []
    for i in range(len(new_mat)):
        if i not in index:
            trans_mat.append(new_mat[i])
        else:
            zeros_mat.append(new_mat[i])

    trans_mat.extend(zeros_mat)
    fmat = []
    for i in range(len(trans_mat)):
        fmat.append([])
        extend_mat = []
        for j in range(len(trans_mat[0])):
            if j not in index:
                fmat[i].append(trans_mat[i][j])
            else:
                extend_mat.append(trans_mat[i][j])
        fmat[i].extend(extend_mat)
    return fmat, len(zeros_mat)


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def simplify(x, y):
    d = gcd(x, y)

    x, y = x//d, y//d
    return Fraction(x, y)


def lcm(a):
    val = a[0]
    for i in range(len(a)):
        val = (val*a[i])//gcd(val, a[i])
    return val


def split_to_QR(mat, r_len):
    Q, R = [], []
    q_len = len(mat) - r_len
    for i in range(q_len):
        Q.append([int(i == j)-mat[i][j] for j in range(q_len)])
        R.append(mat[i][q_len:])
    return Q, R


def tranpose(mat):
    fmat = [[0 for _ in range(len(mat))]for _ in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            fmat[j][i] = mat[i][j]
    return fmat


def multiply(mat1, mat2):
    c = []
    for i in range(len(mat1)):
        c.append([])
        for j in range(len(mat2)):
            c.append(Fraction(0, 1))
            for k in range(len(mat1[0])):
                c[i][j] += mat1[i][k] * mat2[k][j]
    return c


mat = [
    [0, 1, 0, 0, 0, 1],  # s0, the initial state, goes to s1 and s5 with equal probability
    [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4, but with different probabilities
    [0, 0, 0, 0, 0, 0],  # s2 is terminal, and unreachable (never observed in practice)
    [0, 0, 0, 0, 0, 0],  # s3 is terminal
    [0, 0, 0, 0, 0, 0],  # s4 is terminal
    [0, 0, 0, 0, 0, 0],  # s5 is terminal
]
solution(mat)
