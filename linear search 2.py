pos=-1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
          globals()['pos']=i
          return True
        i=i+1
    return False
list=[1,2,3,4,5]
n=4
if search(list ,n):
    print('f ',pos+1)
else:
    print('not found')



def se(l,n):
    i=0
    for i in range(len(l)):
        if n==l[i]:
            print(n,'found in the pos',i)
            break
    else:
        print('not print')
        i+=1    

l=[6,8,9]
n=int(input('enter the no'))
se(l,n)
