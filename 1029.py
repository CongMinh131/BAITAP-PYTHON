def gcd(a,b):
    while (b != 0) :
        c = a % b
        a = b
        b = c
    return a

def kt(s):
    a=int(s)
    s1=s[::-1]
    b=int(s1)
    if(gcd(a,b)==1):
        return 1
    return 0


t=int(input())
while(t>0):
    s=str(input())
    if kt(s)==1:
        print("YES")
    else:
        print("NO")
    t=t-1