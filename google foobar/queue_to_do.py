def solution(start, length):
    if length == 1:
        return start
    checksum = 0
    cur = start
    cur_len = length
    while cur_len > 0:
        checksum ^= XOR(cur) ^ XOR(cur + cur_len)
        cur += length
        cur_len -= 1

    return checksum


def XOR(n):
    if n == 0:
        return 0
    val = (n-1) % 4
    if val == 0:
        return n-1
    elif val == 1:
        return 1
    elif val == 2:
        return n
    elif val == 3:
        return 0


def sol(start, length):
    if length == 1:
        return start
    curr = start
    cur_len = length
    checksum = 0
    n = 0
    while cur_len > 0:
        count = 0
        n += 1
        while count < cur_len:
            print('curr:- ', curr)
            checksum ^= curr
            print('checksum:- ', checksum)
            curr += 1
            count += 1
        cur_len -= 1
        curr = start + n*length
    return checksum


a = int(2000000000**0.5)
print(a)
# print(sol(2, ))
