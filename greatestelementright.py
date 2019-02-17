n=int(input())
l=list(map(int,input().split()))
p=[0]*n
for i in range(n-1):
    p[i]=max(l[i+1:n])
p[-1]=0
for i in p:
    print(i,end=" ")
