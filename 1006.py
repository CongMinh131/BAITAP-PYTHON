def kt(s):
    n=0
    m=len(s)
    for i in range(0,m):
        if s[i]!='4' and s[i]!='7':
            return 0
            break
    return 1
t=int(input())
while(t>0):
    s=str(input())
    if kt(s)==1:
        print("YES")
    else:
        print("NO")
    t=t-1