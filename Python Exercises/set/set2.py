# Find the elements in a given set that are not in another set
#     set1 = {1,2,3,4,5}
#     set2 = {4,5,6,7,8}
#     diffrence between set1 and set2 is {1,2,3}


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
x=set1.difference(set2)
print(x)
y=set2.difference(set1)
print(y)
a=set1 - set2
print(a)
b=set2 - set1
print(b)