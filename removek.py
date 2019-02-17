nk=list(map(int,input().split()))
n=nk[0]
k=nk[1]
l=list(map(int,input().split()))
p=[]
for i in l:
    if(i!=k):
        p.append(i)
if(len(p)==0):
    print('empty')
else:
    for i in p:
        print(i,end=" ")

