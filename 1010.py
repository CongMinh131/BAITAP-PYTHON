t=int(input())
while(t>0):
    s=str(input())
    l=len(s)
    for i in range(0,l):
        if(s[0]==s[l-2] and s[1]==s[l-1]):
            print("YES")
            break
        else:
            print("NO")
            break
    t=t-1