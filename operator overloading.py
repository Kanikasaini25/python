class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __sub__(self,other):
        m1=self.m1-other.m1
        m2=self.m2-other.m2
        s3=student(m1,m2)
        return s3
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return 1
        else:
            return 0
    def __str__(self):
        return self.m1,self.m2
s1=student(8,9)
s2=student(5,6)
s3= s1 - s2
print(s3.m1,s3.m2)
if s1>s2:
     print('s1')
else:
     print('s2')
a=6
print(a)
print(s1.__str__())
     
