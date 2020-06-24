class Calculating:
    first=0
    second=0
    answer=0
    def __init__(self,f,s):
        self.first=f
        self.second=s
        
    def mul(self):
        self.answer=self.first*self.second
        
    def div(self):
        self.answer=self.first/self.second

    def sub(self):
        self.answer=self.first-self.second

    def add(self):
        self.answer=self.first+self.second

    def printing(self):
        print("Frist no is =",self.first)
        print("Second no is =",self.second)
        print("Answer is =",self.answer)
        print("")
        
obj1=Calculating(5,2)
obj1.mul()
obj1.printing()

obj2=Calculating(100,50)
obj2.add()
obj2.printing()