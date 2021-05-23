def fact(A):
    if A == 0 or A== 1:
        return 1
    else:
        fact = 1
        for i in range(1,A+1):
            fact*=i
        return fact

A = [9,9,9]
str_ = ""
for i in A:
    str_+=str(i)
val = int(str_)
val+=1
val = str(val)
print(list(map(int,val)))

print(fact(100))
