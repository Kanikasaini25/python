list=[1,2,3,4,5,6,7,8]
def binarysearch(l,n):
    l=0
    u=len(list)-1
    for i in range(u+1):
        mid=(l+u)//2
        if list[mid]==n:
           print(n,'found at',mid+1)
           break
        elif(list[mid]<n):
           l=mid+1
        elif(list[mid]>n):
           u=mid-1
    else:
        print('not found')
         
n=9
binarysearch(list,n)
