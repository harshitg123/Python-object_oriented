# Data hiding
In Python, we use double underscore (Or __) before the attributes name and those attributes will not be directly visible outside.
    
        class MyClass: 
  
        # Hidden member of MyClass 
        __hiddenVariable = 0
    
        # A member method that changes  
        # __hiddenVariable  
        def add(self, increment): 
            self.__hiddenVariable += increment 
            print (self.__hiddenVariable) 
   
    # Driver code 
    myObject = MyClass()      
    myObject.add(2) 
    myObject.add(5) 
  
    # This line causes error 
    print (myObject.__hiddenVariable)
##### Output :
    2
    7
    Traceback (most recent call last):
      File "filename.py", line 13, in 
        print (myObject.__hiddenVariable)
    AttributeError: MyClass instance has 
    no attribute '__hiddenVariable' 
    
In the above program, we tried to access hidden variable outside the class using object and it threw an exception.

We can access the value of hidden attribute by a tricky syntax:    
    
    # A Python program to demonstrate that hidden 
    # members can be accessed outside a class 
    class MyClass: 
  
        # Hidden member of MyClass 
        __hiddenVariable = 10
  
    # Driver code 
    myObject = MyClass()      
    print(myObject._MyClass__hiddenVariable) 

##### Output :
    10

Private methods are accessible outside their class, just not easily accessible. Nothing in Python is truly private; internally, the names of private methods and attributes are mangled and unmangled on the fly to make them seem inaccessible by their given names.

# Printing Objects
Printing objects gives us information about objects we are working with. In C++, we can do this by adding a friend ostream& operator << (ostream&, const Foobar&) method for the class. In Java, we use toString() method. In python this can be achieved by using \_\_repr\_\_ or \_\_str\_\_ methods.

    class Test: 
        def __init__(self, a, b): 
            self.a = a 
            self.b = b 
  
        def __repr__(self): 
            return "Test a:%s b:%s" % (self.a, self.b) 
  
        def __str__(self): 
            return "From str method of Test: a is %s," \ 
                  "b is %s" % (self.a, self.b) 
  
    # Driver Code         
    t = Test(1234, 5678) 
    print(t) # This calls __str__() 
    print([t]) # This calls __repr__() 
    
##### Output :
    From str method of Test: a is 1234,b is 5678
    [Test a:1234 b:5678]
    
Important Points about Printing:

* If no \_\_str\_\_ method is defined, print t (or print str(t)) uses \_\_repr\_\_.    

      class Test: 
          def __init__(self, a, b): 
              self.a = a 
              self.b = b 
  
          def __repr__(self): 
              return "Test a:%s b:%s" % (self.a, self.b) 
  
      # Driver Code         
      t = Test(1234, 5678) 
      print(t)  
##### Output :
    Test a:1234 b:5678
* If no \_\_repr\_\_ method is defined then the default is used.

      class Test: 
          def __init__(self, a, b): 
              self.a = a 
              self.b = b 
  
      # Driver Code         
      t = Test(1234, 5678) 
      print(t)  
##### Output :
      <__main__.Test instance at 0x7fa079da6710>      
