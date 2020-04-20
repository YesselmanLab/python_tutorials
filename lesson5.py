# Welcome to the fifth lesson in the Yesselman Group's Python series
# Topics covered: Functions
########################################################################################################################
# Part I: Basics
# Since lesson1, we've been using functions to get things done. print(), len() and type() are all great functions, but 
# what do you do if you want a custom function to help prove your Nobel Prize-winning idea? Well, you just write your own!
# Below is an example of a function, uncomment line 12 and see what happens when you run the script:

def helloworld():
  print("Hello World")

# helloworld()

# What happened? What exactly is going on here? Well, on line 9, a function named "helloworld" is defined and then called. 
# Functions have the following format:
#
# def [FUNCTION_NAME]([ARGUMENTS]):
#      [CODE_TO_EXECUTE]
#
# Where:
# + FUNCION_NAME is a name that can have the letters A-Z (and lowercase) _ or 0-9
# + ARGUMENTS are what you give the function in between the parantheses when you call the function (like variables or 
# text in the print() function)
# + CODE_TO_EXECUTE is the block of code that the function "owns". It is tabbed over as with if and for loops
########################################################################################################################
# Part II: Examples, Examples, and More Examples!
# Like most things, functions are better shown than explained, so here are some examples:
# 1. A function that takes two numbers and adds them

def add_numbers(num1,num2):
  print(num1," + ",num2," = ",num1 + num2)
  
n1 = 10
n2 = 20
# add_numbers(n1,n2)

# 2. A function that takes two numbers and RETURNS their product

def multiply(number_1, number_2):
  return number_1*number_2

# print(multiply(10,50))
# Here the return keyword means that after the function finished executing, the function will be replaced with whatever the 
# function "returns". Explain what line 41 should yield given this. Were you correct?
# 3. A function that takes no arguments and returns a value

def get_pi():
  return 3.1415

# 4. A function that takes no arguments and returns nothing

def print_to_100():
  for num in range(100):
    print(num)
    

# Everything we have covered so far can also be used in functions. Consider the following examples:

def factorial(number):
  answer = 1
  while number > 0:
    answer *= number
    number -= 1
  return answer

def legal_base_pairs(input_sequence):
  allowed_pairs = ["A","C","G","U"]
  for nt in input_sequence:
    if nt not in allowed_pairs:
      return False
  return True

# Functions can also call other functions

def print_here():
  print("HERE")

def example_calling_other_fns():
  for i in range(10):
    print_here()

# This is a trival example, but you will definitely write code like the above in the future. Below are a few slightly
# more advanced examples:

def get_maximum(input_list):
    current_max = input_list[0]
    for val in input_list:
      if val > current_max:
        current_max = val
    return current_max

def square_root(input_number):
  if (input_number == 0):
    return 0
  root = input_number/2.
  new_root = root + 1

  while (root != new_root):
    difference = input_number/root

    new_root = root
    root = (root + difference)/2
  return root

########################################################################################################################
# Part III: Some Rules and Techincal Stuff
# Clearly, there are a lot of things you can do with functions. That being said, there are a few final rules to note:
# Rules
# 1. The function cannot have a duplicate name (i.e. you can't name it print() or have two functions with name example())
# 2. You will always call the function with the format name(), even if there aren't any arguments
# 3. The function's actions have to be compatible with whatever you are passing as an argument. For example, if you are 
# writing a function with a for loop, you can give the function a str() or list[], but not an int() or float()
# 4. Python will always try to change the value you give to a function, so make a copy if you don't want to do so (see 
# above example with get_maximum() function)
# Tips
# 1. Give the paramters names that you won't use elsewhere. Ex: use input_number and then don't use input_number elsewhere
# in your code
# 2. Keep your function names less than 30 letters, but try to make them descriptive, for example this
def print_(val):
    for v in val:
       print(v)
# is not a very good name, as print_() is ambiguous to a user. Instead, try something like:
def print_list_elements(input_list):
  for element in input_list:
    print(element)
# This may seem like a small thing, but especially in larger projects you will start to have issues when your functions 
# have ambiguous/non-descriptive names. 
########################################################################################################################
# Homework
# (T/F) The following is a legal function name: tHiS_iS_mY_fUnCtIoN_
# (T/F) A function has to return something
# Bug Buster: Kathy is trying to write some code to find the absolute value of a number. What is wrong with what she has
# written

# number = -1.
# def absolute_value():
#   if number < 0:
#     number *= -1
#   return number

# Easy difficulty problem
# fill out the below function so that it returns a number squared
def squared(input_number):
  pass

# Medium difficulty problem
# fill out the below function so that it returns the minimum value of a list
def min_value_list(input_list):
  pass

# Hard difficulty problem
# write a function is_valid_structure() that takes a secondary structure as a string and returns "True" if the structure is 
# valid and "False" if not
# For it to be valid, it has to contain only the letters "(", ")" and "." and the number of "(" and ")" letters must be the same. 

def is_valid_structure(input_ss):
  pass