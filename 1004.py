def kt(n):
    if (n<2):
        return 0;  
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
def gcd(a,b):
    while (b != 0) :
        c = a % b
        a = b
        b = c
    return a



t=int(input())
while(t>0):
    n=int(input())
    s=0
    for i in range(1,n):
        if(gcd(i,n)==1):
            s=s+1
    if(kt(s)):
        print("YES")
    else:
        print("NO")
    t=t-1

