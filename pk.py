p=[]
k=0
l=list(map(int,input().split()))
l=sorted(l)
for i in range(len(l)):
    c=l.count(l[i])
    if(c>1):
        if(l[i] not in p):
            p.append(l[i])
        i=i+c-1
        k=k+1
if(k==0):
    print("unique")
else:
    for i in p:
        print(i,end=" ")
        

