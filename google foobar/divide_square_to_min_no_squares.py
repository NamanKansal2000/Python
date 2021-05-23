def solution(area):
    l = []
    while(area >= 1):
        x = (int(area**0.5))**2
        l.append(x)
        area = area - x
    return l


print(solution(15324))
