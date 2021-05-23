n = int(input())
l = [5,4,3,2,1]
c = 0
for i in l:
    c+=n//i
    n = n%i

print(c)
