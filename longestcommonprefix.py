n=int(input())
l=[]
m=[]
t=""
f=1
for i in range(n):
    s=input()
    k=len(s)
    m.append(k)
    l.append(s)
minimum=min(m)
for i in range(n-1):
    for j in range(minimum):
        for k in range(i+1,n):
            if(l[i][j]==l[k][j]):
                t=t+l[k][j]
                break
            else:
                f=0
                break
        if(f==0):
            break
    if(f==0):
        break
if(n>2):
    print(t[:len(t)//(n-1)])
else:
    print(t)
    
        

