n=int(input())
l=list(map(int,input().split()))
s=0
j=1
f=0
for i in l:
    s=s+i
    a=s/j
    if(j<n and a==(sum(l)-s)/(n-j)):
        f=1
        break
    j=j+1
if(f==1):
    print('yes')
else:
    print('no')

