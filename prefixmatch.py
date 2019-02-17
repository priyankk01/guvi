n=int(input())
s=input().split()
pre=input()
l=len(pre)
c=0
for i in range(n):
    if(pre==s[i][:l]):
        c=c+1
print(c)
