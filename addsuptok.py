nk=list(map(int,input().split()))
n=nk[0]
k=nk[1]
l=list(map(int,input().split()))
f=0
for i in range(len(l)-1):
    if(l[i]+l[i+1]==k):
        print('yes')
        f=1
        break
if(f==0):
    print('no')
