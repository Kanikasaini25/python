import csv
with open("student.csv","r")as f:
    w=csv.reader(f)
    data=list(w)
    for i in data:
        for j in i:
            print(j,"\t",end="")
        print()    