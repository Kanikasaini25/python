s=input("enter the str")    
m=''
k=''
for i in s:
       if i.isalpha():
              m=m+i
       else:
              k=k+i
print(''.join(sorted(m)+sorted(k)))
       
