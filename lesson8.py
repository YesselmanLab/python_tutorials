# Welcome to the eighth lesson in the Yesselman Group's Python series
# Topics covered: Classes
########################################################################################################################
# Part I: Class Basics
# So far, the lessons have covered how to group and manipulate data via lists/dictionaries and functions. While a lot can
# be achieved with these tools alone, the associated lack of structure and data integrity does not scale well with project
# size or complexity. Luckily, classes come to the rescue and address these issues. Classes are groupings of related data
# and functions designed to modularize programs and improve scalability. This may sound abstract, but you've actually been 
# using python classes since lesson 1! Types like ints, floats, bools and strings are all types of objects. Below is an 
# example of a class declaration for a Student object:

class Student:
    def __init__(self):
        self.name = str()
        self.age = int()

    def set_age(self,age):
        self.age = age

    def set_name(self,name):
        self.name = name

    def show(self):
        print("Student name: {}, Student age: {}".format(self.name, self.age))

# Similar to how you have previously created other types, a student object is created by calling the class's constructor
# as seen below:

my_student = Student()

# In the above code, the class is created by using the "__init__" method, which tells Python how to set up an instance of the
# class. To actually use the class, you will need to use the class's functions, which are also called methods. This is done 
# with the dot (".") operator syntax. The general format is INSTANCE.METHOD_NAME() See the example below:

my_student.set_age(10)
my_student.set_name("David")
#my_student.show()

# Uncomment line 37 to see what happens! The dot operator also allows a class to store variables, often called "attributes".
# The concept here is similar to key-value pairs in dictionaries, although the calling convention is a bit different. Returning
# to the above example, a class is declared using the following syntax:

# class CLASSNAME:
#   [INDENTED IN METHOD DECLARATIONS]

# You have probbaly noticed that each method has a parameter called "self", which refers to the current instance of the object. 
# While it does not have to be named "self", it is common convention to do so, so please abide to improve code readability. 
# Regardless, this parameter is how one can access class members and attributes within the scope of a method declaration. 
########################################################################################################################
# Part II: Writing Your Own Methods
# Writing good methods is key to making a good class. Some general rules of thumb are:
# 1. A method should only do one thing
# 2. A method should be at most 50 lines long
# 3. A method's name should be descriptive but less than ~100 characters

# That being said, there are a few special types of methods to cover. Methods with two leading and trailing underscores are 
# referred to as "special" methods. They are reserved and are listed here (https://www.python-course.eu/python3_magic_methods.php). 
# You've already interacted with __init__() above, which is called a constructor. Constructors provide information about how to 
# make an instance of the object. Below is an example of a Point3 class, which represents a 3D point with an x,y and z value. In 
# this constructor, x,y and z are given default values of 0. 


class Point3:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

# A constructor is generally a good place to initialize values and/or define member attributes and not much else. Ideally, a 
# constructor should do relatively little. An alternative implementation for a constructor could look like the below definition
# for a Point3D. 

class Point3D:
    def __init__(self,x=0.,y=0.,z=0.):
        self.x = x
        self.y = y
        self.z = z

# In python, when a parameter is set equal to a value in the function definition, it serves as a default parameter which is used 
# if no other value is supplied. Long story short, it allows both of the declarations shown below:

default_point = Point3D()
parameterized_poitn = Point3D(1,2,3)

# Note that this syntax also works for regular functions. A final note is that the other magic methods allow you to, among other 
# things, use operators between objects. For example, .__add__() allows you to use "+" signs between objects. Consider the following
# example:

class Money:
    def __init__(self,value):
        self.amount = value

    def __add__(self,other):
        return Money(self.amount + other.amount)

    def __eq__(self,other):
        return self.amount == other.amount

money1 = Money(1.)
money2 = Money(2.)
money3 = Money(3.)

money2 = money2 + money1

print(money2 == money3)
print(money1)
# In reality, most magic methods do not need to be made for a class, but it is useful to understand that operators (a.k.a. +,-,
# \,+=, -=, etc.) are actually just anonymous functions. In practice, two common uses of magic methods are comparison operators 
# and __str__(), which controls how an object will appear if printed to the screen. This can be helpful as by default, Python 
# would just print out something like "<lesson8.Money object at 0x105083e10>", which just tells the object type and its location 
# in memory. By defining the __str__() method, you can control how the class is portrayed in the terminal. Below is an example of 
# a Pet object with some methods and magic methods

class Pet:
    def __init__(self,type,name):
        self.type=type
        self.name=name
        self.weight=5.
        self.hungry=True
    
    def feed(self,food):
        self.weight += food
        self.hungry = False

    def exercise(self):
        self.weight -= 1.

    def __str__(self):
        return "Pet name: {} type: {} weight: {}".format(self.name,self.type,self.weight)

    def __eq__(self,other):
        return self.type == other.type and self.name == other.name and self.hungry == other.name and self.weight == other.weight


dog = Pet("dog","Fido")
dog.feed(10)
# print(dog)
dog.exercise()
# print(dog)
dog2 = Pet("dog","Fido")
# print(dog==dog2)
########################################################################################################################
# Part III: Guidelines for Creating Classes
# Classes are a building block of larger programs, meaning well-designed ones are crucial for good programs. A common 
# mistake is to make classes do too little, or too much. A good rule of thumb is that if a class only has a constructor 
# and a single method, it should probably be a built-in object like a dictionary. This guideline is also relevant for 
# classes that perform minimal transformations on the data they contain and primarily serve to store and change values.
# For example the below TestScore class is better suited as a dictionary of values:

class TestScore:
    def __init__(self,score,grade):
        self.score=score
        self.grade=grade

    def change(self,score,grade):
        self.score=score
        self.grade=grade

# Instead...

score = {
        "score" : 0, # these can be lists if there are multiple scores as well
        "grade"  : "NA"
        }

# On the other end, having more than about 20 class methods (not including magic methods) is also likely a problem. A good guideline
# is that each class should focus on doing one thing. Following this guideline is helpful for modularizing code as having an 
# excessive amount of methods will obscure a class's purpose and functionality. 

# Another good guideline is to avoid directly setting class attributes outside the scope of class methods. A core concept for 
# programming classes is encapsulation, the idea that once a class is given data, it can only be affected through the 
# interface of a class method. This is designed to improve data integrity and ensure it is only altered/accessed in desired ways. 
# Using the above TestScore class example, updating the score with the .change() method is good, whereas diretly accessing the 
# member attributes is bad

# GOOD use of encapsulation
my_score = TestScore(60,"D")
# regrade == better score
my_score.change(80,"B")

# BAD use of direct access
my_score.score = 100

# As you continue to work on projects, you will get a better sense of how to write good classes, but these tips 
# should be very helpful to get started with
########################################################################################################################
# (T/F) A class should have at least 2 methods besides the constructor.
# (T/F) A class is a collection of data and functions.

# Explain what encapsulation is and why it is immportant.

# Bug busters. Laura is trying to write a class to reresent a book. She wants the constructor to take the name of the book 
# as a constructor argument. What does she need to do to fix it?

class Book:
    def __int__(self,bookname):
        self.name = bookname


# Instead of three problems, this homework has a single assignment. Read the below specifications and create a class that meets
# the requirements:

class RNA:
    pass
    # attributes:
    # 1. secondary structure
    # 2. sequence 
    # 3. length
    # 4. A, C, G and U content
    # Methods
    # 1. constructor that takes the the sequence and structure as arguments
    # 2. contains() -> method that takes a substructure string and tells if it is found in the RNA's secondary structure
    # 3. find_content() -> method that calculates the bp % content
    # 4. legal() -> returns boolean. to be legal, secondary structure and sequence must have same length, the secondary structure's
    # 5. longest_A_substring() -> return the length of the longest stretch of A's
    # string must constain only (, . and ), the number of ('s must equal )'s and the sequnce only contains the BPs A, C, G and U
    # 6. __str__() -> be creative and come up with an informative string representation of the object
    # 7. __eq__() -> here you have to test what would make two RNA's equal to eachother
