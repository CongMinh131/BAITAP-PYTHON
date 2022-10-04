n = int(input()) 
a = [int(i) for i in input().split()] 
a.sort() 
res = a[0] 
flag =1 
for i in a: 
    if i!= res : 
        print(res) 
        flag=0 
        break 
    res=res+1  
if flag: print(a[-1]+1)