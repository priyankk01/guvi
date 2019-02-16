mn=list(map(int,input().split()))
m=mn[0]
n=mn[1]
p=[]
d=[]
for i in range(m):
    l=list(map(int,input().split()))
    p.append(l)
    d.append(l)
for i in range(m):
    if(0 in d[i]):
        p[i]=[0]*n
for i in range(m):
    for j in range(n):
        if(d[i][j]==0):
            for k in range(m):
                p[k][j]=0
for i in range(m):
    for j in range(n):
        print(p[i][j],end=" ")
    print()