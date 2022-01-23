book={}
book['a']=
{
    "name":"k",
    "phn":12345678',
    "add":"dfgh"
}
book['b']=
{
    "name":"h",
    "phn":1234567878',
    "add":"dfg4567"
}
import json
a=json.dumps(book)
with open("c/user/kanika saini/json.txt","w") as f: #string format
    f.write(a)
    
...........read the file
with open("c/user/kanika saini/json.txt","r") as f:
    f.read()  # string format
    
    
import json
k=json.load(book)
print(k) # dict format
    
    
