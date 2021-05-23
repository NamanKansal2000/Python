def solve(s):

    s = s.strip()
    lst = []
    str = []
    lst = s.split()
    for i in lst:
        str.append(i.capitalize())
    temp = (' ').join(str)
    return temp

s = input()
result = solve(s)
print(result)
