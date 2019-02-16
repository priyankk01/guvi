n=int(input())
s=list(map(int,input().split()))
f=list(map(int,input().split()))
m=1
for i in range(n-1):
    for j in range(i+1,n):
        if(s[j]>=f[i]):
            i=j
            m=m+1
            break
    if(i==n-1):
        break
print(m)
    
