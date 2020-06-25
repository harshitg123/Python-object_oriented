# Inheritance in Python
Inheritance is the capability of one class to derive or inherit the properties from another class. The benefits of inheritance are:

  1. It represents real-world relationships well.
  2. It provides reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
  3. It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

Below is a simple example of inheritance in Python

    # A Python program to demonstrate inheritance  
   
    # Base or Super class. Note object in bracket. 
    # (Generally, object is made ancestor of all classes) 
    # In Python 3.x "class Person" is  
    # equivalent to "class Person(object)" 
    class Person(object): 
       
        # Constructor 
        def __init__(self, name): 
            self.name = name 
   
        # To get name 
        def getName(self): 
            return self.name 
   
        # To check if this person is an employee 
        def isEmployee(self): 
            return False
   
   
    # Inherited or Subclass (Note Person in bracket) 
    class Employee(Person): 
   
        # Here we return true 
        def isEmployee(self): 
            return True
   
    # Driver code 
    emp = Person("Geek1")  # An Object of Person 
    print(emp.getName(), emp.isEmployee()) 
   
    emp = Employee("Geek2") # An Object of Employee 
    print(emp.getName(), emp.isEmployee()) 
##### Output:
    Geek1 False
    Geek2 True

## What is object class?
Like Java Object class, in Python (from version 3.x), object is root of all classes.

In Python 3.x, “class Test(object)” and “class Test” are same.
In Python 2.x, “class Test(object)” creates a class with object as parent (called new style class) and “class Test” creates old style class (without object parent). Refer this for more details.

Subclassing (Calling constructor of parent class)
A child class needs to identify which class is its parent class. This can be done by mentioning the parent class name in the definition of the child class.
Eg: class subclass_name (superclass_name):
. . . 
. . . 

    # Python code to demonstrate how parent constructors 
    # are called. 
  
    # parent class 
    class Person( object ):     
  
            # __init__ is known as the constructor          
            def __init__(self, name, idnumber):    
                    self.name = name 
                    self.idnumber = idnumber 
            def display(self): 
                    print(self.name) 
                    print(self.idnumber) 
  
    # child class 
    class Employee( Person ):            
            def __init__(self, name, idnumber, salary, post): 
                    self.salary = salary 
                    self.post = post 
  
                    # invoking the __init__ of the parent class  
                    Person.__init__(self, name, idnumber)  
  
                  
    # creation of an object variable or an instance 
    a = Employee('Rahul', 886012)     
  
    # calling a function of the class Person using its instance 
    a.display()  
##### Output:
    Rahul
    886012

‘a’ is the instance created for the class Person. It invokes the \_\_init\_\_() of the referred class. You can see ‘object’ written in the declaration of the class Person. In Python, every class inherits from a built-in basic class called ‘object’. The constructor i.e. the ‘\_\_init\_\_’ function of a class is invoked when we create an object variable or an instance of the class.

The variables defined within \_\_init\_\_() are called as the instance variables or objects. Hence, ‘name’ and ‘idnumber’ are the objects of the class Person. Similarly, ‘salary’ and ‘post’ are the objects of the class Employee. Since the class Employee inherits from class Person, ‘name’ and ‘idnumber’ are also the objects of class Employee.

If you forget to invoke the \_\_init\_\_() of the parent class then its instance variables would not be available to the child class.

The following code produces an error for the same reason.

    # Python program to demonstrate error if we 
    # forget to invoke __init__() of the parent. 
  
    class A: 
        def __init__(self, n = 'Rahul'): 
            self.name = n 
    class B(A): 
        def __init__(self, roll): 
            self.roll = roll 
  
    object = B(23) 
    print (object.name) 
##### Output :
    Traceback (most recent call last):
      File "/home/de4570cca20263ac2c4149f435dba22c.py", line 12, in 
        print (object.name)
    AttributeError: 'B' object has no attribute 'name'
