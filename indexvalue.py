n=int(input())
l=list(map(int,input().split()))
p=[]
f=0
for i in range(n):
    if(l[i]==i):
        f=1
        p.append(l[i])
p=sorted(p)
if(f==1):
    for i in p:
        print(i,end=" ")
else:
    print(-1)
        
