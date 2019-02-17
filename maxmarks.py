m=input().split('#')
n=input().split('#')
s=0
p=0
for i in range(3):
    s=s+int(m[i+1])
    p=p+int(n[i+1])
if(s>p):
    print(m[0])
if(p>s):
    print(n[0])
       
