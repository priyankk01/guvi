n=input()
l=list(map(int,input().split()))
m=max(l)
mi=min(l)
for i in range(len(l)):
    if(l[i]==mi):
        print(i+1,end=" ")
for i in range(len(l)):
    if(l[i]==m):
        print(i+1,end=" ")

