
def kt(n):
    if (n<2):
        return 0;  
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

t=int(input())
while(t>0):
    s=str(input())
    l=len(s)
    for i in range(0,l):
        s1=s[l-4]+s[l-3]+s[l-2]+s[l-1]
    a=int(s1)
    if kt(a)==1:
        print("YES")
    else:
        print("NO")
    t=t-1
