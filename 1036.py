t=int(input())
while(t>0):
    n=int(input())
    s=0
    if(n%2==0):
        a=2
        while(n>=a):    
            s=float(s+1/a)
            a=a+2
    elif(n%2==1):
        a=1
        while(n>=a): 
            s=float(s+1/a)
            a=a+2
    print(round(s,6))
    t-t-1

