def kt(l1,l2):
    for i in range(0,len(s1)):
        a=int(l1[i])
        b=int(l2[i])
        if(a>b):
            return 0
    return 1
t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    s1=input().split()
    s2=input().split()
    l1=[];l2=[]
    for i in range(0,len(s1)):
        l1.append(int(s1[i]))
    for i in range(0,len(s2)):
        l2.append(int(s2[i]))
    l1.sort()
    l2.sort()
    
    if(kt(l1,l2)):
        print("YES")
    else: 
        print("NO")