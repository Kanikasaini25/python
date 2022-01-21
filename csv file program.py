import csv
with open("student.csv","w") as f:
    w=csv.writer(f)
    w.writerow(["name","sub","no"])
    n=int(input("enter the no of student"))
    for i in range(n):
        n=input("enter the student name")
        s=input("enter the student sub")
        no=input("enter the student no")
        w.writerow([n,s,no])
print("sucessfully")        
        
    