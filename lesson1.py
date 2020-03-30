# Welcome to the first lesson in the Yesselman Group's Python series
# Topics covered: What is Python?, How Python Works, Hello World and Intro to Variables
# first, lets get through some of the basics...
########################################################################################################################
# Part I: What is Python?
# Python is a high-level scripting language used in a variety of disciplines including: websites, science, servers, analytics
# and many others. The language was created in 1990 and started to see significant growth post 2010 to being one of the
# most popular languages today.
# What is Python good at?
# Python is a great choice for automating simple tasks (i.e. copying files), moving and analyzing data, making graphics.
# A lot of the language's strengths are in its flexibility and the wide variety of open source libraries that have been
# developed in the community.
# What is Python NOT good at?
# Python is relatively slow compared to other languages like C or Java, so for intense applications (i.e. reading terabytes
# of data, making billions of calculations), it is usually a bad choice. There are still ways to improve performance when
# desired, but this is the ultimate cost of the language's ease of use.
########################################################################################################################
# Part II: How Python Works
# Python is like most programming languages where a set of instructions (code) is written in a text file and then executed
# by the computer. It's worth noting that python reads just like we do, left to right and down the page. To run a program,
# the following code is used (note that the carrot implies this is being called from the terminal).
# >python [code file's name]
# That's it! So, the general flow of making python programs is:
# 1. Write the code you want to run and save it into a file with a .py extension
# 2. Call the code from the terminal with format >python [file name]
# But enough talk about Python, lets just get to doing some programming!
########################################################################################################################
# Part III: Hello World and Intro to Variables
# You may or many not know already, but this file is actually python code. As seen above, when the '#' sign is on a line,
# python ignores whatever comes after. These are called comments. Uncomment the below line and run this python script as
# described in Part II. What do you get?

#print("Hello World")

# Congrats on running your first program! Here you are using a function (more on those later), but print() is a very
# useful one that "prints" information to the terminal. Above you are just using it to print out text, but you can also
# use it to print out just about any information you want to.

# Variables in python are very similar to variables in Math. Variables are assigned values and can then be manipulated
# in a variety of ways. Uncomment the following code and see what you get:

# number1 = 1
# print(number1)
# print(number1*2)
# number2 = number1 + 3
# print(number2)
# number2 = number2/3
# print(number2)
# number3 = 5*3
# print(number3)
# print(2**2)
# The biggest difference so far between the syntax of math and python it the equals sign '='. In python, this is called
# the assignment operator and is used to give a variable a value. It is generally used in the following format:
# variable_name = value. Because the variable has to be set to a new value, the code number1 + 1 won't change the value
# of number1. To add one to this value, you have to use the assignment operator in the following format:
# number1 = number1 + 1
# This may look a little odd, but it makes sense if you sub in the 'old' value of number1. In python there is a shorthand
# for adding one to a number, namely
# number1 += 1
# which means take the value of number1 and add one. The '+=' symbol is accompanied by '-=', '/=' and '*='. What do you
# think they do?
########################################################################################################################
# Quiz/Homework
# (T/F) There are very few libraries available for python.
# (T/F) Python reads code right to left.
# You are thinking about making a bunch of charts and graphics for a presentation. Is python a good choice?
#
# You need to quickly analyze 1.5 TB of genomic data. Is python a good choice for this project?
#
# Read the following code and guess what the output will be. Uncomment the print line and see the answer. Were you correct?
inches_in_foot = 12
feet_in_yard = 3
yard_in_football_field = 100
inches_in_football_field = inches_in_foot*feet_in_yard*yard_in_football_field

# print(inches_in_football_field)
# Create a variable to show your current age. Print this to the console. Increment this value and print the before and
# after to the terminal. Try with both the '+' and '+=' operators.