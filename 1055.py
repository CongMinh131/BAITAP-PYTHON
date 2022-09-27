
def kt(s):
    for i in range(2,len(s)):
        if(i%2==0):
            if(s[i-2]==s[i] and s[0]==s[len(s)-1]):
                return 1
    return 0

t = int(input())
while t > 0:
    t -= 1
    s=str(input())
    if len(s)%2==1 and s[0]!=s[1] and kt(s)==1 :
        print("YES")
    else:
        print("NO")
    