# Classes and Objects

## Classes
A class is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

To understand the need for creating a class let’s consider an example, let’s say you wanted to track the number of dogs which may have different attributes like breed, age. If a list is used, the first element could be the dog’s breed while the second element could represent its age. Let’s suppose there are 100 different dogs, then how would you know which element is supposed to be which? What if you wanted to add other properties to these dogs? This lacks organization and it’s the exact need for classes.

Class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object.

### some points on python class
* Classes are created by keyword class.
* Attributes are the variables that belong to class.
* Attributes are always public and can be accessed using dot (.) operator. Eg.: Myclass.Myattribute

      Class Definition Syntax:
      
      class ClassName:
      # Statement-1
      .
      .
      .
      # Statement-N
      
### Defining a class –
      
      # Python program to  
      # demonstrate defining  
      # a class 
    
      class Dog: 
      pass
      
# Objects
An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values. It’s not an idea anymore, it’s an actual dog, like a dog of breed pug who’s seven years old. You can have many dogs to create many different instances, but without the class as a guide, you would be lost, not knowing what information is required.

An object consists of :

* State : It is represented by attributes of an object. It also reflects the properties of an object.
* Behavior : It is represented by methods of an object. It also reflects the response of an object with other objects.
* Identity : It gives a unique name to an object and enables one object to interact with other objects.
![](img-1.png)
### Declaring Objects (Also called instantiating a class)
When an object of a class is created, the class is said to be instantiated. All the instances share the attributes and the behavior of the class. But the values of those attributes, i.e. the state are unique for each object. A single class may have any number of instances.

Example:
![](img-2.png)
### Declaring an object –
    # Python program to 
    # demonstrate instantiating 
    # a class 
  
  
    class Dog:  
      
        # A simple class 
        # attribute 
        attr1 = "mamal"
        attr2 = "dog"
  
        # A sample method   
        def fun(self):  
            print("I'm a", self.attr1) 
            print("I'm a", self.attr2) 
  
    # Driver code 
    # Object instantiation 
    Rodger = Dog() 
  
    # Accessing class attributes 
    # and method through objects 
    print(Rodger.attr1) 
    Rodger.fun() 
    
##### Output:
    mamal
    I'm a mamal
    I'm a dog
In the above example, an object is created which is basically a dog named Rodger. This class only has two class attributes that tell us that Rodger is a dog and a mammal.    

## Some points that we should take care of when we are dealing with Classes and Objects.

### 1. What is the "*self*"?

 * Class methods must have an extra first parameter in method definition. We do not give a value for this parameter when we call the method, Python provides it.
 * If we have a method which takes no arguments, then we still have to have one argument.
 * This is similar to this pointer in C++ and this reference in Java.

  When we call a method of this object as *myobject.method(arg1, arg2)*, this is automatically converted by Python into *MyClass.method(myobject, arg1, arg2)* – this is all the   special self is about. 
 
 ### 1. What is "*\_\_init\_\_*" method?
 
  The \_\_init\_\_ method is similar to constructors in C++ and Java. Constructors are used to initialize the object’s state. Like methods, a constructor also contains a         collection of statements(i.e. instructions) that are executed at the time of Object creation. It is run as soon as an object of a class is instantiated. The method is useful   to do any initialization you want to do with your object.
    
        # A Sample class with init method  
    class Person:  
    
        # init method or constructor   
        def __init__(self, name):  
            self.name = name  
    
        # Sample Method   
        def say_hi(self):  
            print('Hello, my name is', self.name)  
    
    p = Person('Nikhil')  
    p.say_hi()  
#### Output:
    Hello, my name is Nikhil
    
# Class and Instance Variables

Instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class. Instance variables are variables whose value is assigned inside a constructor or method with self whereas class variables are variables whose value is assigned in the class.

Defining instance varibale using constructor.

    # Python program to show that the variables with a value   
    # assigned in the class declaration, are class variables and  
    # variables inside methods and constructors are instance  
    # variables.  
     
    # Class for Dog  
    class Dog:  
    
        # Class Variable  
        animal = 'dog'             
    
        # The init method or constructor  
        def __init__(self, breed, color):  
      
            # Instance Variable      
            self.breed = breed 
            self.color = color         
     
    # Objects of Dog class  
    Rodger = Dog("Pug", "brown")  
    Buzo = Dog("Bulldog", "black")  
  
    print('Rodger details:')    
    print('Rodger is a', Rodger.animal)  
    print('Breed: ', Rodger.breed) 
    print('Color: ', Rodger.color) 
  
    print('\nBuzo details:')    
    print('Buzo is a', Buzo.animal)  
    print('Breed: ', Buzo.breed) 
    print('Color: ', Buzo.color) 
  
    # Class variables can be accessed using class  
    # name also  
    print("\nAccessing class variable using class name") 
    print(Dog.animal)         
##### Output:
    Rodger details:
    Rodger is a dog
    Breed:  Pug
    Color:  brown

    Buzo details:
    Buzo is a dog
    Breed:  Bulldog
    Color:  black

    Accessing class variable using class name
    dog
Defining instance variable using the normal method.

    # Python program to show that we can create   
    # instance variables inside methods  
     
    # Class for Dog  
    class Dog:  
        
        # Class Variable  
        animal = 'dog'      
        
        # The init method or constructor  
        def __init__(self, breed):  
            
            # Instance Variable  
            self.breed = breed              
    
        # Adds an instance variable   
        def setColor(self, color):  
            self.color = color  
        
        # Retrieves instance variable      
        def getColor(self):      
            return self.color     
    
    # Driver Code  
    Rodger = Dog("pug")  
    Rodger.setColor("brown")  
    print(Rodger.getColor())   
##### Output:
    brown
