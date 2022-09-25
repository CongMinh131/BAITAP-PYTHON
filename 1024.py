def tong(s):
    n=int(s)
    t=0
    while(n>0):
        t=t+n%10
        n=int(n/10)
    return t

def kt(s):
    for i in range(0,len(s)-1):
        a=int(s[i])
        b=int(s[i+1])
        c=a-b
        if(abs(c)!=2):
            return 0
        return 1

        
t=int(input())
while(t>0):
    s=str(input())
    if tong(s)%10==0 and kt(s):
        print("YES")
    else:
        print("NO")
    t=t-1