# Welcome to the ninth lesson in the Yesselman Group's Python series
# Topics covered: External Modules and File IO
########################################################################################################################
# Part I: External Module Basics
# At this point, you are able to: define variables, control flow with conditional statements, iterate, write functions,
# and make classes. But... any code you write has to be in a single .py file. This is a major drawback as large files can
# quickly become difficult/impossible to maintain. In python, this can be circumvented with an import statement, which 
# allows you to import another file/module's functions and classes. Uncomment line 12 and run this script to see what happens:

import testmodule 

#testmodule.helloworld()

# There are a few ways to import external modules to your python file. Below are some common ways and associated descriptions:

# import [MODULE] 

# Generic way to import a module. As seen above, all functions/classes are used with the format MODULE.FUNCION() or MODULE.CLASS()

# import [MOULE] as [ALIAS]

# Simiilar to the generic way, except that the module is given an alias, usually because the module's official name is very long. 
# The alias helps as calling a function or class is done with the format ALIAS.FUNCTION() or ALIAS.CLASS(). An example of 
# this is the graphing module matplotlib.pyplot, which is frequently imported as plt. Which is easier to call? matplotlib.pyplot.plot()
# or plt.plot()?

# from [MODULE] import [FUNCTION,CLASS,etc]

# This syntax allows you to import specific functions or classes that can be called on their own without the MODULE prefix. Be
# careful though, as this can lead to issues if there are naming conflicts in your local file.

# from [MODULE] import *

# This syntax allows you to import anyting in a module that does not have a name that starts with an underscore. This method is 
# generally not recommended as it can easily lead to naming conflicts with the current or other modules. 
########################################################################################################################
# Part II: Local vs Distributed Modules 
# There are two main types of modules: local and distributed. Local modules are simply .py files that you have written. To use 
# them, they have to be in the same directory as the python script you are calling. Given a file with the name MODULE.py, 
# the import statement is "import MODULE". Above we imported the lcoal testmodule.py as testmodule. This module also contains
# a TestClass class. In the space below, create an instance of this class and call its method ".show()"



# Distributed modules are ones that either come with python or have to be installed to your machine. Distributed modules can 
# be accessed by python files from anywhere in the computer. This is different from local modules as moving to a different 
# directory would make the reference to the module un-resolvable. Python comes with a lot of useful modules out of the box
# like math, random, re, glob and many more (look up some of those modules to see what they do!). Sometimes you will want a 
# module that you do not have installed on your computer. To install the module, you can use the command 
# "pip install [MODULE] --user" in your terminal. Pip is python's package management system and should give you some 
# screen updates when the install is proceeding as desired. 

# Note: Depending on how your PyCharm (or other IDE) is set up on your computer, you may have the situation where the 
# modules installed on your computer's python and PyCharm's python are not the same. There are ways to deal with this, 
# but a common issue to run into is where code works in PyCharm but not in the terminal or vice versa. 
########################################################################################################################
# Part III: Best Practices When Using Modules
# Modules are an extremely powerful way to compartmentalize code and functionality. When used properly they can help 
# projects scale and improve code validity. Used improperly, however, modules can cripple a project with unccessary 
# complexity and headaches. Below are some general guidelines for effective module usage:
# 1. All module imports should be at the TOP of a python file. This makes it easy to see everything that is in being used
# in a file and track module dependencies within a project. 
# 2. When designing a project, each file .py file should contain at most one class definition. 
# 3. If a project uses a variety of functions, it is often a good idea to group them together into a "Utils" file. 
# 4. If you are only using a single function from a module, the from [MODULE] import [FUNCTION] syntax.
########################################################################################################################
# Part IV: File IO
# While the input() and print() functions can be useful for giving and receiving information to and from a python program, 
# these methods have significant drawbacks as they are generally slow and tend to not work well for large data. To solve
# these and other problems, programs often read and write information from files. File input-output (IO) in python is 
# centered around the open() function. Open takes two arguments, the file name, which specifies the target file, and the
# mode, which indicates how the file will be manipulated. The mode codes are as follow:

# "r" -> read-only plaintext
# "w" -> write-only plaintext, deletes existing content or creates a new file if doesn't already exist
# "a" -> append-only plaintext, adds new text to the end of the file
# "rb" -> read-only binary
# "wb" -> write-only binary, deletes existing content or creates a new file if doesn't already exist
# "ab" -> append-only binary, adds new binary information to the end of the file

# In addition to the above modes, there are permutations with the "+" letter, but those will not be covered for now. For 
# the time being, the "r" and "w" modes will cover almost all usage. Below is an example of opening a plaintext file and 
# then reading out the contents to the screen. Uncomment line 88 to see what the file contains:

textfile = open("examplefile.txt","r")
contents = textfile.read()
textfile.close()
# print(contents)

# The above code highlights the three major steps in file IO: 
# 1. opening the desired file in the desired mode
# 2. reading/writing the desired information from/to the file
# 3. closing the file 

# An alternate syntax for file IO is as follows:

with open("examplefile.txt", "r") as infile:
    pass
    # print(infile.read())

# Here, the close statement is omitted as python automatically closes the file when exiting the with statement. As with 
# other control statements, everything within the with statement has to be tabbed-over. There are a few main ways to extract
# text from a file:

# read() -> returns a string with all of the file's text
# readlines() -> returns a list of strings with each string corresponding to a line. note this often leaves newlines ('\n') in
# readlin() -> returns a single line of text from the target file

# in practice the below code is usually the best way to get the raw lines out of a file

with open("numbers.txt", "r") as numbers:
    for line in numbers.read().splitlines():
        pass
        # print(line)

# Writing to a file is usually pretty simple. You can only write strings and writing is done with the .write() method. See
# the below example

my_data = ["data1",1,2,3,4]

with open("textfile.txt", "w") as outfile:
    for data in my_data:
        outfile.write(str(data)+ '\n')

# It is important to remember that everything being read in is still just a string, even though it may look like a different 
# datatype. From this, you must be sure to perform the necessary conversions.
########################################################################################################################
# Homework
# This homework builds on the previous week's and the RNA class you previously made, so be sure that the class is up 
# functioning properly

# For this assignment, you will be making a new file called ParseRNAs.py, which will have two main functions:
# 1. read_rnas() -> this function will take a file path as a parameter and will return a list of RNA objects. The file path
# will be for a file with the following format:
# SEQUENCE1, STRUCTURE1
# SEQUENCE2, STRUCTURE2
# ..., etc
# The repo includes an example of an input file, "rnas.csv"
# 2. export_rnas() -> this function takes a list of RNA objects as a parameter and returns nothing. If the RNA is legal, it
# will have its sequence and structure written to "legal.csv" and if they are not they will be added to "illegal.csv". When
# writing the RNA objects, use the above format of "SEQUENCE,STRUCTURE" for each line for each RNA. 
