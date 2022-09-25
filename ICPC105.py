
def Solution(s):
    num=0;res=0
    l=len(s)     
    for i in range(0,l):
        if (s[i] >= '0' and s[i] <= '9'):
            a=int(s[i])
            b=int('0')
            num = num * 10 + (a-b);          
        else:
            res = max(res,num);            
            num = 0
    return max(res,num)

t=int(input())
while t>0:
    s=str(input())
    print(Solution(s))
    t=t-1
