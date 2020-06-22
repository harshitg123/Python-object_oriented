# Program for basic under standing 
# Classes and object

class dog:
    
    # Class variable
    animal="dog"
    
    # init method or constructor
    def __init__(self,bread):
        self.bread=bread # instance variable
        
    # method
    def setcolour(self,colour):
        self.colour=colour # instance variable
        
    # method
    def getcolour(self):
        return self.colour # instance variable

Rodger=dog("pug")
Rodger.setcolour("brown")
print(Rodger.getcolour())