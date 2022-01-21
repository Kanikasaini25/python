class mycham:
    def f1(self):
        print('write')
        print('run')
        print('output')
class pycham:
    def f1(self):
        print('write')
        print("compile")
        print('run')
class c:
    def code(self,idle):
        idle.f1()
        
idle = mycham()        
l = c()
l.code(idle)
              
