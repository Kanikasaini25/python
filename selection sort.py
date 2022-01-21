n=int(input('enter the size'))
l=[]
for i in range(n):
    v=int(input('enter the no'))
    l.append(v)
print(l)
def sort(l):
    for i in range(n):
          minpos=i
          for j in range(i,n):
            if l[j]<l[minpos]:
              minpos=j
          t=l[i]
          l[i]=l[minpos]
          l[minpos]=t

sort(l)
print(l)
                
