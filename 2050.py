
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    s=input().split()
    l=[]
    s1=s[::-1]
    for i in range(0,len(s1)):
        cnt=1
        if(int(s[i])>int(s[i+1])):
            cnt=cnt+1
        print(cnt,end=" ")
