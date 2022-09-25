

from pickletools import float8
from tokenize import Double

def tong(n,a):
    while(n>=a):    
            s=float(s+1/a)
            a=a+2
    return s

t=int(input())
while(t>0):
    n=int(input())
    s=0
    if(n%2==0):
        tong(n,2)
    elif(n%2==1):
        tong(n,1)
    print(round(s,6))
    t-t-1

