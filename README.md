# Yesselman Group Coding Lessons
This repository features a set of python lessons for use in onboarding people to the Yesselman Lab at UNL. They are to be accessible to beginners and assume zero programming experience. Part I focuses on Python
## **Part I: Python**
### lesson0 : Setting everything up
#### Terminal for Windows Users
For Windows users, it is recommended to download the [Cmder](https://cmder.net/) terminal emulator to use instead of the native Windows command prompt. Cmder runs on top of the Windows OS and helps to bridge the gap to the preferred UNIX terminals. To install, just click on the provided link and follow the instructions on the website. You will know it is working properly when you can launch the colorful terminal.
#### Downloading and Installing Python
To download python, go the following [link](https://www.python.org/downloads/) and click the button at the top of the page to download the latest version. Select the appropriate platform (Mac, Windows, Linux, etc.) and follow the directions provided. You can test that python is properly downloaded by entering python in the terminal as below:

`>python`

If python is installed, the terminal should enter the python command line interpreter and look something like this (though parts of the header will likely look different):

```
Python 3.7.7 (default, Mar 10 2020, 15:43:33)
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
To exit, simply type in 
`>>>exit()`
and hit enter. If nothing happens, this is likely because your computer does not know where python is located. This is a more common issue on Windows platforms and some common work arounds can be found [here](https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/). Help for Mac users can also be found [here](https://docs.python-guide.org/starting/install3/osx/).

#### Setting up Pycharm
The Yesselman Group's integrated development environment (IDE) of choice is PyCharm, which is developed by JetBrains. As students, you are eligible for an educational license to use the professional version, which you can apply for [here](https://www.jetbrains.com/community/education/#students). While waiting for your license, you can download the [PyCharm community edition](https://www.jetbrains.com/pycharm/download/#section=mac). Click on the aforementioned link, select your platform and you can download the Community version immediately!

### lesson1 : What is Python?, How Python Works, Hello World and Intro to Variables
#### Covers:
+ background information on python and programming
+ generic python workflow
+ Hello World program that would make K&R proud
+ the use of variables to store and manipulate data
### lesson2 : Native types in Python, If statements
#### Covers:
+ descriptions of `int()`,`float()`,`str()` and `bool()` types as well as operators
+ warnings about mixing `int` and `float` types as well as associated narrowing
+ syntax and conventions for `if` statements
+ nesting of `if` statements and multibranching
### lesson3 : Lists
#### Covers:
+ methods to add, remove and manipulate entries in `list()` objects
+ indexing and the use of the `[]` operator
### lesson4 : For and while loops
#### Covers:
+ basic looping for both `for` and `while` loops
+ combinding looping and conditionals
+ using `break` for extra control flow
### lesson5 : Functions
+ anatomy of functions -> name, return types, parameters
+ how to write user defined functions
+ more detail on function calling
### lesson6 : Sets and Strings
+ intro to the `set()` object, with an emphasis on use in summarizing datasets
+ revisit strings and string maninpulation, covering the following methods:
	+ `.split()`
	+ `.join()`
	+ `.find()`
	+ `.trim()`
### lesson7 : Dictionaries
+ literal declaration of `dict()` objects 
+ manipulating key-value pairs with the `[]` operator
+ iterating through dict entries with `.values()`,`.keys()` and `.items()`
### lesson8 : Classes
+ how to write a `class`
+ discussion of attributes, methods and magic methods
+ explanation of best practices for writing effective classes
+ does NOT cover polymorphism/inheritance
### lesson9 : External Modules and File IO
### lesson10 : Unittesting
### lesson11 : Data Analysis I: Intro to Pandas
### lesson12 : Data Analysis II: Intro to Matplotlib
