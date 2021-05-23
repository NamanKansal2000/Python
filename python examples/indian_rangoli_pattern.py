# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e        when size = 5
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


import string


def print_rangoli(size):
    # your code goes here
    # Upper triangle
    N = size
    mid = N - 1

    for i in range(N - 1, 0, -1):
        row = ['-'] * (2 * N - 1)
        for j in range(N - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))

    for i in range(0, N):
        row = ['-'] * (2 * N - 1)
        for j in range(0, N - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
