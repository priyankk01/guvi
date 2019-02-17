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
    out.append((l[r[i][0]-1:r[i][1]]))
for j in range(q):
    res=out[j][0]
    for i in range(len(out[j])-1):
        res=res^out[j][i+1]
    print(res)

