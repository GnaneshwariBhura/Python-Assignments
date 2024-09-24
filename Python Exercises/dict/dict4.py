# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21

country=['china','india','usa','pakistan']
population=[143,136,32,21]
d=dict()
i=0
while i<len(country):
    d[country[i]]=population[i]
    i+=1
print(d)
# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
keys=d.keys()
keys=list(keys)
print("Enter the input: ")
a=input()
if a=="print":
    for i in keys:
        print(i,"==>",d[i])
elif a=="add":
    print("enter the country name to add")
    cname=input()
    if cname in keys:
        print(d[cname])
    else:
        print("Enter the population of that country")
        popu=int(input())
        d[cname]=popu
        print(d)
# when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
elif a=="remove":
    print("Enter the country to remove")
    cname=input()
    if cname in keys:
        d.pop(cname)
        print(d)
    else:
        print("Doesn't Exist")
    