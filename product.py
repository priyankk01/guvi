n=int(input())
A=list(map(int,input().split()))
out=[]
p=1
for i in A:
    p=p*i
for i in A:
    out.append(p//i)
for i in out:
    print(i,end=" ")
