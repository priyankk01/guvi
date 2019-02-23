n=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(n-1):
    c=1
    for j in range(i,n-1):
        if(l[j]<l[j+1]):
            c=c+1
        else:
            break
    p.append(c)
print(max(p))
    

