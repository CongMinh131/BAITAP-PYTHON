
t = int(input())
while t > 0:
    t -= 1
    s=str(input())
    res=1
    for i in range(0,len(s)):
        if( s[i]!="0"):
            res=res*int(s[i])
    print(res)
    