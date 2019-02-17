n=int(input())
p=[]
for i in range(n):
    l=list(map(int,input().split()))
    p.append(l)
res=[]
for i in range(n):
    for j in range(len(p[i])):
        res.append(p[i][j])
res=sorted(res)
for i in res:
    print(i,end=" ")
        
