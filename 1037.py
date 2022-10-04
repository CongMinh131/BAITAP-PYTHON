import math

def kt(n,i):
    if(n%i==0):
        return 1
    return 0

t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    res=0;cnt=0
    if(n==1):
        res=1
    for i in range(1,n+1):
        if(kt(n,i)==1):
            res=res+1
    for i in range(1,n):
        for j in range(1,i):
            if(kt(i,j)==1):
                cnt=cnt+1
    print(res,cnt)
        
