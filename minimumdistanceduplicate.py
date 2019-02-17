n=int(input())
l=list(map(int,input().split()))
uv=list(map(int,input().split()))
u=uv[0]
v=uv[1]
p=[]
q=[]
r=[]
for i in range(n):
    if(l[i]==u):
        p.append(i)
    if(l[i]==v):
        q.append(i)
for i in p:
    for j in q:
        if(i-j>0):
            r.append(i-j)
        if(j-i>0):
            r.append(j-i)
print(min(r))
        
        

