t=int(input())
while(t>0):
    s=str(input())
    l=len(s)
    for i in range(0,l):
        if s[l-2]=='8' and s[l-1]=="6":
            print("YES")
            break
        else:
            print("NO")
            break
    t=t-1