def gcd(a,b):

    if(b==0):
        return a
    return gcd(b,a%b)

t=int(input())
while(t>0):
    s1=str(input())
    s2=str(input())
    a=int()
