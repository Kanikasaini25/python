n=input("enter str")
v='a','e','i','o','u'
l=[]
for i in n:
       if i in v:
              if i not in l:
                     l.append(i)
print(l)

      
