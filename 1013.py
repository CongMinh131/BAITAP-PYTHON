from ast import Return


def nt(n):
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
def tong(a,b):
    m=gcd(a,b)
    s=0
    while(m>0):
        s=s+m%10
        m=int(m/10)
    return s

t=int(input())
while(t>0):
    a,b=map(int,input().split())
    if(nt(tong(a,b))):
        print("YES")
    else:
        print("NO")
    t=t-1