class con:
    def __init__(self):
        self.cons="default constructor"
    
    def print_cons(self):
        print("In this example init is not taking any parameter so it is",self.cons)
        
check=con()
check.print_cons()