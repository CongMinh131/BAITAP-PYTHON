s=str(input())
s1=s[::-1]
l=len(s1)
t=0;n=0
for i in range(0,l):
    if(l%3==1 and t==1):
        print(",",end="")
        t=0
    elif(l%3==2 and t==2):
        print(",",end="")
        t=0
    if(l%3==0 and t==3 ):
        print(",",end="")
        t=0
    if(t==3):
        print(",",end="")
        t=0
    t=t+1
    print(s1[i],end="")
