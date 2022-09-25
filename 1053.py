def kt(s):
    l=len(s)
    for i in range(0,l):
        if s[i]!="0" and s[i]!="1" and s[i]!="2":
            return 0
    return 1

t=int(input())
while(t>0):
    s=str(input())
    l=len(s)
    if kt(s)==1:
        print("YES")
    else:
        print("NO")
    t=t-1