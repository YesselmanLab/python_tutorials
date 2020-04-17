# Welcome to the fourth lesson in the Yesselman Group's Python series
# Topics covered: For and While loops
########################################################################################################################
# Part I: The For Loop
# So far, you've learned how to assign data to variables and manipulate these individual variables(conditionally if desired). 
# Likewise, you know how to use lists to store large amounts of data, but how can you manipulate large amounts of data?
# The answer: For Loops. In python, Loops are used to repeat blocks of code a set number of times, with the For loop being
# the most common. Python For Loops are used to access the elements of an "iterable" object (like a list, for instance). Here,
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
########################################################################################################################
# Part II: The While Loop
# Unlike the For loop, which iterates over a list or similar object, a While loop executes a block of code as long as a boolean
# statement is true. It has the following structure:
#
# While [Boolean]:
#   [code to execute'
#
# Below is a rewrite of the above "Hello world" For loop. Uncomment it and see what happens.
# hw_count = 0
# while hw_count < 100:
#   print("Hello World")
#   hw_count +=1 # what happens if this is deleted? 
#
# often times, you can achieve a repitive process with a While or For Loop, but it is useful to know how to do both. A unique
# ability of the While loop is to do "infinite" looping. Consider the following code. Will it ever stop?
#
# while True:
#   print("Will this loop stop?")
########################################################################################################################
# Part II: Combinining Loops and If statements
# When used together, Loops and If statements give you the ability to rapidly manipulate data in a conditional manner. 
# Consider the following example:

test_values = [1,2,3,4,5,6,7,8,9,10]

for value in test_values:
    if value%2 == 0:
    # print(value, " is even")
    else:
    # print(value, " is odd")
    
# In addition to analyzing data, for loops can be used to generate data. The following makes a "checkerboard" string:

checker_board = ""

for row in range(5):
    for col in range(5):
       if (row*5 + col)%2 == 0:
          checker_board += "X"
       else:
          checker_board += " "
     checker_board += "\n"
# print(checker_board)
# Somtimes, you also want to break out of a loop when some condition is met. This is done with the "break" keyword, as shown
# below:

rna_sequence = "GGACGCUTA"
allowed_bps = ["A", "C", "G", "U"]

for bp in rna_sequence:
  if bp not in allowed_bps:
    # print(bp," is not an allowed bp")
    break

