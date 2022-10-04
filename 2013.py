import sys
def kt(n):
    cnt=1
    while(n>1):
        if n%2==0:
            n=int(n/2)
        else:
            n=n*3+1
        cnt=cnt+1
    return cnt
while(1):
    n=int(input())
    if(n!=0):
        print(kt(n))
    else:
        break
    



