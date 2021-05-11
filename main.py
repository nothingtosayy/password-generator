# generating random password

#password = rubna123
import string
import random
a = string.ascii_lowercase
b = string.ascii_uppercase
c = string.digits
password = random.sample(a+b+c,8)
print("Generated Password : ","".join(password))

#without using import string
list1 = []
for i in range(65,91):
    list1.append(chr(i))
m = "".join(list1)
list2 = []
for j in range(97,123):
    list2.append(chr(j))
n = "".join(list2)
list3 = []
for k in range(0,10):
    list3.append(str(k))
p = "".join(list3)
print("Generated Password : ","".join(random.sample(m+n+p,8)))


