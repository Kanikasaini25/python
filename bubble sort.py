def sort(num):
    n=len(num)
    for i in range(n-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                t=num[j]
                num[j]=num[j+1]
                num[j+1]=t
                print(num)
num=[4,6,8,7,1,2]
sort(num)
print(num)
