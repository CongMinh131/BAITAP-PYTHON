from queue import Empty


t=int(input())
k=0;cnt=0;l=[]
while(t>0):
    t=t-1
    kt=0
    s=input().split()
    if(s!=Empty):
        cnt=cnt+1
    if(cnt==4):
        k=k+1
        if(cnt==1 and len(s)==6):
            l.append(1)
        elif(cnt==1 and len(s)==7):
            kt=2
            l.append(2)
        cnt=0
print(k)
for i in range(0,len(l)):
    print(l[i])

