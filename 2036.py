


def nt(n):
    if (n<2):
        return 0;  
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

n=int(input())
s=input().split()
l=[]
for i in range(0,len(s)):
    a=int(s[i])
    l.append(a)
l.sort()
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        a=int(l[i])
        b=int(l[j])
        if(gcd(a,b)==1):
            print(a,b)

