t = int(input())
for _ in range(t):
    s = int(input())
    p = s%12
    if p == 0:
        p = 12
    c = 13-p
    val = ''
    if c in [1,12,6,7]:
        val = 'WS'
    if c in [2,11,5,8]:
        val = 'MS'
    if c in [3,10,4,9]:
        val = 'AS'
    print(c+s-p, val)
