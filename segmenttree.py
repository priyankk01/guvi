nq=list(map(int,input().split()))
n=nq[0]
q=nq[1]
l=list(map(int,input().split()))
r=[]
out=[]
for i in range(q):
    p=list(map(int,input().split()))
    r.append(p)
for i in range(q):
    out.append(sum(l[r[i][0]-1:r[i][1]]))
for i in out:
    print(i)
    

