nk=list(map(int,input().split()))
n=nk[0]
k=nk[1]
A=list(map(int,input().split()))
f=0
for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        if(A[i]+A[j]==k):
            print('YES')
            f=1
            break
    if(f==1):
        break
if(f==0):
    print('NO')
        