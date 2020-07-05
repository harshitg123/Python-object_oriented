class person( object ):
    def __init__(self,name,id_no):
        self.name=name
        self.id_no=id_no
    
class employee( person ):            
    def __init__(self, name, id_no): 
            self.salary = "50 lpa" 
            self.post = "software" 
  
            # invoking the __init__ of the parent class  
            person.__init__(self, name, id_no)  
  
    def display(self):
        print("name  :",self.name)
        print("id    :",self.id_no)
        print("post  :",self.post)
        print("salary:",self.salary)
    
    def isemployee(self):
        return ("It is employee")
    

obj=employee("Harshit gupta",44)
obj.display()
print(obj.isemployee())
        