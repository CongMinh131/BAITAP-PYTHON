a,k,n=map(int,input().split())
s=0
m=int(n/k)
for i in range(1,m+1):
    x=k*i-a
    if(x>=0):
        print(x)
        s=1

if(s==0):
    print("-1")