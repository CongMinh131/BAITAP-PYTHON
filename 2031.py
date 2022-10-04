def nt(n):
    if (n<2):
        return 0;  
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
def kt(s):
    for i in range(0,len(s)):
        c=int(s[i])
        if(nt(c)):
            s[i]=1
        else:
            s[i]=0
        print(s[i],end=" ")
t=input().split()
a=int(t[0])
while(a>0):
    s=input().split()
    kt(s)
    print("\n")
    a=a-1

