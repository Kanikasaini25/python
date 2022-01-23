import random
l="sdfghjrtyuiovbnmiofhjk"
u="ASDFGHJKGHJKLDFGHJKSDFGH"
S="@#$$^&*"
n="2345678"
a=l+u+S+n
l=5
password="".join(random.sample(a,l))
print(password)