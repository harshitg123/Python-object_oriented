# Types of Inheritance
Types of Inheritance depends upon the number of child and parent classes involved. There are five types of inheritance in Python:

__1. Single Inheritance:__ Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and addition of new features      to existing code.

![](img-1.PNG)

**Example:**

    # Python program to demonstrate 
    # single inheritance 
  
    # Base class 
    class Parent: 
         def func1(self): 
              print("This function is in parent class.") 
  
    # Derived class 
    class Child(Parent): 
         def func2(self): 
              print("This function is in child class.") 
  
    # Driver's code 
    object = Child() 
    object.func1() 
    object.func2() 
##### Output :-
    This function is in parent class.
    This function is in child class.
**2. Multiple Inheritance:** When a class can be derived from more than one base classes this type of inheritance is called multiple inheritance. In multiple inheritance, all the      features of the base classes are inherited into the derived class.
![](img-2.PNG)

**Example:**
 
    # Python program to demonstrate 
    # multiple inheritance 
  
  
    # Base class1 
    class Mother: 
        mothername = "" 
        def mother(self): 
            print(self.mothername) 
  
    # Base class2 
    class Father: 
        fathername = "" 
        def father(self): 
            print(self.fathername) 
  
    # Derived class 
    class Son(Mother, Father): 
        def parents(self): 
            print("Father :", self.fathername) 
            print("Mother :", self.mothername) 
  
    # Driver's code 
    s1 = Son() 
    s1.fathername = "RAM"
    s1.mothername = "SITA"
    s1.parents() 
##### Output:
    Father : RAM
    Mother : SITA
    
**3. Multilevel Inheritance:** In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to      a relationship representing a child and grandfather.
![](img-3.PNG)

**Example:**

    # Python program to demonstrate 
    # multilevel inheritance 
  
    # Base class 
    class Grandfather: 
        grandfathername =""  
        def grandfather(self): 
            print(self.grandfathername) 
  
    # Intermediate class 
    class Father(Grandfather): 
        fathername = "" 
        def father(self): 
            print(self.fathername) 
  
    # Derived class 
    class Son(Father): 
        def parent(self): 
            print("GrandFather :", self.grandfathername) 
            print("Father :", self.fathername) 
  
    # Driver's code 
    s1 = Son() 
    s1.grandfathername = "Srinivas"
    s1.fathername = "Ankush"
    s1.parent() 
##### Output:

    GrandFather : Srinivas
    Father : Ankush
    
**4. Hierarchical Inheritance:** When more than one derived classes are created from a single base this type of inheritence is called hierarchical inheritance. In this program,      we have a parent (base) class and two child (derived) classes.
![](img-4.PNG)

**Example:**

    # Python program to demonstrate 
    # Hierarchical inheritance 
  
    # Base class 
    class Parent: 
        def func1(self): 
            print("This function is in parent class.") 
  
    # Derived class1 
    class Child1(Parent): 
        def func2(self): 
            print("This function is in child 1.") 
  
    # Derivied class2 
    class Child2(Parent): 
        def func3(self): 
            print("This function is in child 2.") 
   
    # Driver's code 
    object1 = Child1() 
    object2 = Child2() 
    object1.func1() 
    object1.func2() 
    object2.func1() 
    object2.func3() 
##### Output:
    This function is in parent class.
    This function is in child 1.
    This function is in parent class.
    This function is in child 2.
    
**5. Hybrid Inheritance:** Inheritence consisting of multiple types of inheritence is called hybrid inheritence.
![](img-5.PNG)

**Example:**

    # Python program to demonstrate 
    # hybrid inheritance 
  
    class School: 
        def func1(self): 
            print("This function is in school.") 
   
    class Student1(School): 
        def func2(self): 
            print("This function is in student 1. ") 
   
    class Student2(School): 
        def func3(self): 
            print("This function is in student 2.") 
   
    class Student3(Student1, School): 
        def func4(self): 
            print("This function is in student 3.") 
   
    # Driver's code 
    object = Student3() 
    object.func1() 
    object.func2() 
##### Output:
    This function is in school.
    This function is in student 1. 
    
