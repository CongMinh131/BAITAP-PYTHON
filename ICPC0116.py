t=int(input())
while t>0:
    s=str(input())
    l=len(s)
    if(s[0]==s[l-1]):
        print("YES")
    else:
        print("NO")
    t=t-1