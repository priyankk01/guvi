n=int(input())
l=list(map(int,input().split()))
p=[]
f=0
for i in l:
    if(i not in p):
        p.append(i)
    else:
        f=1
        print(i)
        break
if(f==0):
    print("unique")

