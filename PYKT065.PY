def nt(n):
    if (n<2):
        return 0;  
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
def kt(s,n):
    cnt=0
    l=int(s[0])
    r=int(s[1])
    for i in range(l,r+1):
        if(nt(i) and i!=2 and i!=3 and i!=5 and i!=7):
            cnt=cnt+1
        elif(i==1):
            cnt=cnt+1
    return cnt
while(1):
    s=str(input())
    if(s=="-1"):
        break
    l=s.split(" ")
    n=int(input())
    print(kt(l,n))
    