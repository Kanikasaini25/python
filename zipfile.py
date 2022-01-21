from zipfile import *
f=ZipFile("files.zip","r",ZIP_STORED)
name=f.namelist()
for i in name:
       print("file name",i)
       print("the content of the file is:")
       f1=open(i,"r")
       print(f1.read())
f.close()
print("s")
