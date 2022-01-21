class a:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __avg__(self,a= None,b=None,c=None):
         s=0
         if a!=None and b!=None and c!=None:
             s=a+b+c/3
         elif a!=None and b!=None :
             s=a+b/2
         else :
             s=a
         return s    
s1=a(2,3)
print(s1.__avg__(1,2,4))
print(s1.m1,s1.m2)
