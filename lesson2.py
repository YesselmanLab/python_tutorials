# Welcome to the second lesson in the Yesselman Group's Python series
# Topics covered: Native types in python, if statements
########################################################################################################################
# Part I: Python's Native Types
# Python comes with a bunch of builtin dataypes or "types" for short. Types are a key building block of any program, so
# understanding their basic properties and features is very important. Additionally, as part of the Yesselman Group you
# will probably work with C++, which places a lot of significance on types, so it's important you feel comfortable with
# them!
# The four basic types in Python are int (integer), float (decimal number), str (text) and boolean (true/false)
# A float is probably what you think of as normal number and it can store numeric information less than 1 and greater than 0, i.e.
float1 = float(0.01)
# is a legal statement. The above variable declaration looks a bit different than "float1 = 0.01" but is equivalent. Setting
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

# The last thing of note about integers is that in python 2, division yields the number of times the divisor could go into the dividend
# Uncomment the line below and run the script for an example: 
# print(20/3) # note the different output for python3
# How do you get the remainder for such a division? The mod "%" operator (note that there is also a %= operator, feel free to
# explore how it works!!).
# See the below example:
# print(20%3)

# The third basic type is the string, which is equivalent to text. Below are two examples of string declarations
string1 = "I am"
string2 = str(" understanding types in Python")

# Like other types, some mathematical symbols are available for strings. For example, the addition sign concatenates
# strings together. What do you think the code below prints? Uncomment and see:

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
# conditions, which brings us to the If statement.
########################################################################################################################
# Part II: The If Statement
# When writing programs, you will often want to have the behavior of your code depend on various conditions. This is where
# the if statement comes in. An if statement has the following format:
#               if [boolean statement]:
#                   [code to execute]
# It's that simple. There are a few syntax elements to note:
# 1. the line with the if statement must be ended with a colon
# 2. everything in the [code to execute] block must be indented from the if statement
# This is a little pedantic, so lets just do an example:

my_num = 1

if my_num == 1: # statement ends with :
    my_num += 1 # code to execute is indented by one tab compared to the if statement
    print(my_num)

# So, because my_num == 1 (is equal to 1), the code block is executed, where my_num is incremented and then the value (2) is printed to
# terminal. The importance of indenting is that if the code is not indented, it will just be executed, regardless of
# the condition's status. It is important to note that comparisons do not convert types if they are different. i.e. comparing
# a str and int will always evaluate to false, even if they reprsent the same value. ==> "1" == 1 False!!!! There are two other parts of 
# the if statement to worry about, elif : and else: . Below is an example of how to use these additional "branches"

my_num = 5

if my_num == 1:
    print("my_num is 1")
elif my_num == 2:
    print("my_num is 2")
else:
    print("my_num is greater than 2")

# The last thing to cover here is that you can also nest if statements, where another if block is put inside the first
# and so on. Note that the nested if statement has to be tabbed in, and twice ditto for its code blocks that will be
# executed:

num_1 = 10

if my_num < 20:
    if my_num > 5:
        print("number is greater than 5 and less than 20")
    else:
        print("number is less than 5 or equal to 5")
else:
    print("number is greater than or equal to 20")

# play with the above code a bit before moving on to the following homework problems:
########################################################################################################################
# Homework problems
# (T/F) Both integers and floats can store tenths of numbers
# (T/F) In python, 5/2 evaluates to 2
# (T/F) The + and * operators can be used to add together and multiply strings
# Why don't you want to write code like below?
# num1 = 1.
# num2 = 1
# print(num1 == num2)

# Write code that finds and prints the remainder when 1,000,000 is divided by 7.

# Write code that creates a string that has 100 "A"'s followed by 70 "B"'s and prints it to the console.

# Bug Busters. What is wrong with the following code? uncomment it and see if you are correct.

# number1 = 1
#
# if number1 < 10:
#     number1 = 10
#
# print(number1)
#
# if number1 == 10:
#     number1 += "1"
#
# print(number1)

# Challenge problem: Don't worry too much about the semantics of the "for" loop (that will be covered in a future lesson),
# but the goal here is to write an if statement where the "pass" is that takes in a single letter and prints out its identity
# if it is an RNA nucleotide (i.e. A, C, G, U) or not.

rna_sequence = "GCUAGCCUAAAAUCUTUAA"

for nucleotide in rna_sequence:
    # "nucleotide" is the single letter, keep in mind that the code has to be indented by 1 tab 
    pass
