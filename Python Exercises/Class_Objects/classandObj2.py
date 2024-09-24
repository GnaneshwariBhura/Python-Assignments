# Use del property to first delete id attribute and then the entire object

class employee:
    name:None
    id=None
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def work(self):
        print(self.name,"is Working")
        
e=employee("Jhon",2707)
# e=employee("Mark",2708)
# print(e.name , e.id)
e.work() #this will print the statements which inside the function work
del e.id
print(e.name,e.id)
del e #it deletes the complete object which is created
# print(e)# here it give the error that e is not found because we have deleted the object "e"