n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
p=[]
for i in l:
    p.append(str(i))
print("->".join(p))
    

