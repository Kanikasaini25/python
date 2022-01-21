l=[6,2,0,1,3]
for i in range(len(l)):
     while l[i-1]>l[i] and i>0:
        l[i-1],l[i]=l[i],l[i-1]
        i-=1
     print(l)

