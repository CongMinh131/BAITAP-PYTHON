def nt(n):
    if (n<2):
        return 0;  
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
def kt(s):
    c=0;k=0
    for i in range(0,len(s)):
        a=int(s[i])
        if(nt(a)):
            c=c+1
        else:
            k=k+1
    if(c>k):
        return 1
    return 0

t=int(input())
while(t>0):
    s=str(input())
    l=len(s)
    if nt(l)==1 and kt(s):
        print("YES")
    else:
        print("NO")
    t=t-1