from itertools import permutations
nkt=list(map(int,input().split()))
l=list(map(int,input().split()))
n=nkt[0]
k=nkt[1]
t=nkt[2]
p=permutations(l,k)
q=[]
for i in list(p):
    q.append(sum(i))
if(t in q):
    print('YES')
else:
    print('NO')

