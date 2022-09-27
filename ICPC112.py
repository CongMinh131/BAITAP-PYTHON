
def nt(n):
    if (n<2):
        return 0;  
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    res=0
    for i in range(2,n):
        if nt(i)==1 and nt(i+6)==1 and n>i+6:
            if(nt(i+2)==1):
                res=res+1
            elif(nt(i+4)==1):
                res=res+1
    print(res)