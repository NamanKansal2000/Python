n=int(input())
while 1:
    n+=1
    if n%3!=0 and (str(n).find('3')) == -1:
        print(n)
        break
