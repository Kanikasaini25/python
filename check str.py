m=[10,20 ,'asd',30,40,'dfg',10]
sum=0
for n in m: 
       if str(n)==n: 
            continue
       elif int(n)==n:
              sum+=n
       else:
              pass
print(sum)              
