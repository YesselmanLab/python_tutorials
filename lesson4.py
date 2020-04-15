# Welcome to the fourth lesson in the Yesselman Group's Python series
# Topics covered: For and While loops
########################################################################################################################
# Part I: The For Loop
# So far, you've learned how to assign data to variables and manipulate these individual variables(conditionally if desired). 
# Likewise, you know how to use lists to store large amounts of data, but how can you manipulate large amounts of data?
# The answer: For Loops. In python, Loops are used to repeat blocks of code a set number of times, with the For loop being
# the most common. Python For Loops are used to access the elements of an iterable object (like a list, for instance). Here,
# an iterable is just something that has divisible parts. Consider the below example:

num_list = [1,2,4,6,7,65,5]

for number in num_list:
  print(number)
  
# What does the above code do? How would you change it so that the numbers only print if the number is less than 5? 
# The For loop has the following format and similar indentation rules to if loops:

# for [item] in [iterable_object]:
#     [code to execute]

# A useful tool for doing something a set number of times is the range() function. The range takes an integer and makes a 
# list from 0 to n-1 i.e. range(4) => [0,1,2,3]. Consider the following code that prints "Hello World" 100 times:

# for i in range(100):
#   print("Hello World")

# Part II: The While Loop
# Unlike the For loop, which iterates over 
