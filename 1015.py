def kt(s):
    l=len(s)
    for i in range(0,l-1):
        a=int(s[i])
        b=int(s[i+1])
        if(a>b):
            return 0
    return 1

t=int(input())
while(t>0):
    s=str(input())
    if(kt(s)==1):
        print("YES")
    else:
        print("NO")
    t=t-1