n=int(input())
l=list(map(int,input().split()))
p=[]
s=0
for i in range(n-1):
    s=s+l[i]
    m=l[i]
    for j in range(i+1,n):
        s=s+l[j]
        if(s>m):
            m=s
    p.append(m)
    s=0
p.append(l[-1])
print(max(p))
            
        
        
