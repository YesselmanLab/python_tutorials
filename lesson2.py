# Welcome to the second lesson in the Yesselman Group's Python series
# Topics covered: Native types in python, if statements
########################################################################################################################
# Part I: Python's Native Types
# Python comes with a bunch of builtin dataypes or "types" for short. Types are a key building block of any program, so
# understanding their basic properties and features is very important. Additionally, as part of the Yesselman Group you
# will probably work with C++, which places a lot of significance on types, so it's important you feel comfortable with
# them!
# The four basic types in Python are int (integer), float (decimal number), str (text) and boolean (true/false)
# A float is probably what you think of as normal number and it can store numeric information less than 0, i.e.
float1 = float(0.01)
# is a legal statement. The above variable declaration looks a bit different than "float = 0.01" but is equivalent. Setting
# a variable equal to a value without the "float()" part is called a literal declaration. It is generally preferable to
# use the above syntax as it improves readability. Sometimes, you will want a decimal number that is currently a whole number.
# In this case, you should write the number with a decimal point at the end so the computer knows it is not an integer
# This yields a float
float2 = 10.
# This yields an int
int1 = 10
# Before jumping into integer declarations, we'll cover a new function, type(). type() is useful because it tells you what
# the a variable's type is. Combining this with print() can be useful if you are unsure of a variable's type. Uncomment
# the lines below and run this script to see how this combo works

# print(type(int1))
# print(type(float2))

# Integers are very similar to floats in declarations, but it is worth noting that they "narrow" i.e. you lose any information
# about decimal places. Uncomment the line below and see what it prints

# print(int(1.8))

########################################################################################################################
# This is a key point: Converting a float to an int can lead to a loss of precision, usually without a warning, so
# you should always be sure you using the variable types you want to be.
########################################################################################################################
# The last thing of note about integers is that division yields the number of times the divisor could go into the dividend
# Uncomment the line below and run the script for an example:
# print(20/3)
# How do you get the remainder for such a division? The mod "%" operator. See the below example:
# print(20%3)

# The third basic type is the string, which is equivalent to text. Below are two examples of string declarations
string1 = "I am"
string2 = str(" understanding types in Python")

# Like other types, some mathematical symbols are available for strings. For example, the addition sign concatenates
# strings together. What do you think the code below prints? Uncomment and see

#print(string1 + string2)

# For now, the only other one you need to worry about is the multiplication symbol, "*". It Leads to a repeat of a string.
# Uncomment the following statement and see how this works.

# print("|"*100)

# As with the other types, "*=" and "+=" still work. Play around with them a bit to see how these work.

# The last basic type to know is the boolean. The boolean is the simplest data type and can only be true or false. Below
# is an example of a few types of declarations
bool1 = bool(True)
bool2 = (1 == 2)

# The "==" symbol is called the comparison operator and is how you do a boolean literal declaration. The comparison operator
# evaluates to True if the right and left values are equal or False is they are not. The "!=" symbol does the opposite.
# There are other logical operators that will be covered in future lessons, but booleans are good for comparisons or setting
# conditions, which brings us to the if statement.
########################################################################################################################
# Part II: The If Statement
# When writing programs, you will often want to have the behavior of your code depend on various conditions. This is where
# the if statement comes in. An if statement has the following format:
#               if [boolean statement]:
#                   [code to execute]
# It's that simple. There are a few synatx elments to note:
# 1. the line with if statement must be ended with a colon
# 2. everything in the [code to execute] block must be indented from the tab index of the if statement (what??)
# This is a little pedantic, so lets just do an example:

my_num = 1

if my_num == 1: # statement ends with :
    my_num += 1 # code to execute is indented by one tab compared to the if statement
    print(my_num)

# So, because my_num == 1, the code block is executed, where my_num is incremented and then the value (2) is printed to
# terminal. The importance of indenting is that if the code is not indented, it will just be executed, regardless of
# the condition's status. It is important to note that the comparison must be between compatible types. i.e. comparing
# a str and int won't work. ==> "1" == 1 BAD!!!! There are two other parts of the if statement to worry about,
# elif : and else: . Below is an example of how to use these additional "branches".

my_num = 5

if my_num == 1:
    print("my_num is 1")
elif my_num == 2:
    print("my_num is 2")
else:
    print("my_num is greater than 2")

