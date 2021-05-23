def roman(str, n):
    dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    i = 0
    while i < n:
        curr = dict[str[i]]
        print('curr: ', curr)
        if(i+1 < n):
            next = dict[str[i+1]]
            print('next: ', next)
            if curr >= next:
                result+= curr
                i += 1
            else:
                result += next-curr
                i += 2
            print('result: ', result)
        else:
            result+= curr
            i+=1
            print('result: ', result)
    print(result)

str = 'CXLLIVX'
roman(str, len(str))
