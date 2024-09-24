# employee :
#     id
#     name

class employee:
    name:None
    id=None
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def work(self):
        print(self.name,"is Working")
        
e=employee("Jhon",2707)
e=employee("Mark",2708)
print(e.name , e.id)
e.work()