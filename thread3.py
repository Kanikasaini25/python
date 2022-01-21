import threading
import os
def t1():
    print("t1 assingned to thread: {}". format(threading.current_thread().name))
    print("id of process running t1: {}" . format(os.getpid()))
def t2():
    print("t2 assingned to thread: {}". format(threading.current_thread().name))
    print("id of process running t2: {}" . format(os.getpid()))
if __name__=="__main__":
        print("id of process running main program: {}" . format(os.getpid()))
        print(" Main thread name: {}" . format(threading.current_thread().name))
t1=threading.Thread(target=t1,name='t1')        
t2=threading.Thread(target=t2,name='t2')

t1.start()

t2.start()
t1.join()
t2.join()
