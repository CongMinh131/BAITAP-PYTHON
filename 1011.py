def tn(n):
    s = str(n)
    s1 = s[::-1]
    if (s != s1 ):
        return 0
    return 1

def kt(n):
    s = str(n)
    for i in range(0,len(s)):
        if(s[i]!=0 or s[i]!=2 or s[i]!=4 or s[i]!=6 or s[i]!=8):
            return 0
    return 1

t=int(input())
while(t>0):
    n=int(input())
    for i in range(0,n):
        if(tn(i)==1 and kt(i)==1):
            print(i,end=" ")
    t=t-1

