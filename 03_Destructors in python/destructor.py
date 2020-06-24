class des:
    # run's when object created
    def __init__(self,a,b):
        print("Hello,there it's python")
        self.a=a
        self.b=b
    
    # run's when program ended
    def __del__(self):
        print("destructor is called")
        print("sum is:",self.a+self.b)
        
add=des(int(input()),int(input()))
