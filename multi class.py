class a:
    def f1(self):
        print('f1')
    def f2(self):
        print('f2')
class b:
        def f3(self):
           print('f3')
        def f4(self):
           print('f4')
class c(a,b):
    
    def f6(self):
        print('f6')

        
a1=a()
a1.f1()
a1.f2()
b1=b()
b1.f4()
b1.f3()
c1=c()
c1.f3()
c1.f1()
