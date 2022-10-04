def nt(n):
    if(n==0):
        return 1
    elif(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
n,x=map(int,input().split())
m=0;k=x
i=0
while(m<=n):
    if(nt(i)):
        k=k+i
        print(k,end=" ")
        m=m+1
    i=i+1

    