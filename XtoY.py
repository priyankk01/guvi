s=input().split()
m=0
for i in s[0]:
    if(i not in s[1]):
        m=m+1
for i in s[1]:
    if(i not in s[0]):
        m=m+1
print(m)
