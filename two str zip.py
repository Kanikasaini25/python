s=input("enter the str")    
k=input("enter the str")
i,j=0,0
l=" "
while i<len(s) or j<len(k):
       if i<len(s):
              l=l+s[i]
              i=i+1
       if j<len(k):
              l=l+k[j]
              j+=1
print(l)              
