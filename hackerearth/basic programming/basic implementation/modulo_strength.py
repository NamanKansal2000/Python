n,k=map(int,input().split())
a=map(lambda x:int(x)%k,input().split())
d={}
for i in a:
    d[i]=d.get(i,0)+1
c=0
for i in d.keys():
    c+=d[i]*(d[i]-1)
print(c)
