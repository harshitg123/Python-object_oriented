# Basic example of Inheritance

class A( object ):
    def __init__(self,name):
        self.name=name
        
class B(A):
    def __init__(self):
        A.__init__(self,"Harshit Gupta")
        self.roll=44
        
    def display(self):
        print("Name   :",self.name)
        print("roll no:",self.roll)

obj=B()
obj.display()
