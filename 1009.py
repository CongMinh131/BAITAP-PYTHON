
s=str(input())
t=len(s)
n=0;m=0
for i in range(0,t):
    if(s[i].islower()):
        n=n+1
    elif(s[i].isupper()):
        m=m+1
if(n>=m):
    print(s.lower())
else:
    print(s.upper())
