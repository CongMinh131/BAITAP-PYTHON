s=str(input())
n=0
m=len(s)
for i in range(0,m):
    if s[i]=='4' or s[i]=='7':
        n=n+1
if n==4 or n==7:
    print("YES")
else:
    print("NO")