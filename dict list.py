d={}
n=int(input("enter the no"))
for i in range(n):
       n=input("enter the name")
       m=int(input("enter the mrk"))
       d[n]=m
print(d)       
print("name of student","\t","% of marks")
for j in d:
       print("\t",j,"\t\t",d[j])
       
sum=0

for j in d.values():
       sum=sum+j
print(sum)       
