def greatestno(a,b,c):
      if a>b and a>c:
              print("greatest no",a)
      elif b>a and b>c:
              print("greatest no",b)
      else:
              print("greatest no",c)
greatestno(3,8,9)

print('next')

def gn(a ,b,c):
      print(a if a>b and a>c else b if b>c else c)
gn(2,9,5)    
      
