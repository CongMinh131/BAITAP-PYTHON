


t=int(input())
while(t>0):
    a,b,c=map(float,input().split())
    x=c/a
    y=1+b/100
    for i in range(0,10000000):
        if(y**i>=x):
            print(i)
            break
    t=t-1
