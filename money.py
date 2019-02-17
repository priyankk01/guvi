n=int(input())
th=n//1000
n=n%1000
fh=n//500
n=n%500
h=n//100
n=n%100
f=n//50
n=n%50
t=n//10
o=n%10
print(th+fh+h+f+t+o)

