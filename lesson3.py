# Welcome to the third lesson in the Yesselman Group's Python series
# Topics covered: Lists
########################################################################################################################
# Part I: List basics
# As you have seen so far, variables are a great way to store information. That being said, it can be very cumbersome to
# write out a large number of variables. Imagine you have to store test scores for every student in Chem 109 (probably
# about 1300). Writing out that many variables would take a very long time (see below):
# score1 = XX
# score2 = XX
# ...
# score1300 = XX
# There has to be a better way, right? Enter Lists. In Python, a list is a "container" that holds other data inside it.
# Lists are extremely useful in python because they allow easy store and access of data. Below are two examples of how to
# make lists. What do you think the code on lines 19 and 20 will print? Uncomment them and see.

my_list = [1,2,3,4,5]
my_list2 = list([6,7,8,9,10])

#print(my_list)
#print(my_list2)

# The basic syntax is [list_name] = [ elements ]. Note the elements HAVE to be surrounded with square brackets. Because
# lists have no value themselves, it is often important to know their size. In python the function that finds a list's
# size is len(). It has syntax very similar to type(). What do you think the following statements will print? Uncomment them
# and see:
#
# print(len(my_list))
# print(len(my_list2))
########################################################################################################################
# Part II: Adding elements to a list
# Now that you have an idea of what lists are, it's time to talk about the four main ways to create them:
# Method 1: Literal declarations
# Literal declarations were shown above. Like strings, booleans, ints, etc, you can always declare a list directly with
# specific elements as above. On a side note, the contents of a list can be very diverse. They can be different types or
# even other lists! See below for some examples of list declarations:

multitype_list = ["first", 2, 3, 4, 10.059, True]
two_dimensional_matrix = [[1,2,3,4], [5,6,7,8]]

# you can get pretty creative with these declarations so please explore them a bit!

# Method 2: Appending
# Appending is a way to add another element at the end of a list. Below is an example of appending a value to a list

my_list3 = [0,1,2]
#print(len(my_list3))
my_list3.append(3)
#print(len(my_list3))

# What do you think will be printed? Uncomment and see. It should be noted that when you append to a list, you always
# increase the size of the list by 1.

# Method 3: Concatenating with the "+=" operator
# The "+" and "+=" operators work very similarly with lists as they do with strings. Namely, the "+" operator adds together
# two lists and the "+=" adds the right hand side list to the left hand side one. Below are two examples:

#print(my_list + my_list2)
my_list4 = [9,9,9,9,9]
my_list4 += [-1,-1,-1,-1]
#print(my_list4)

# Method 4: Repeating an element
# As with strings, lists can be repeated by using the "*" and "*=" operators. Namely, these operators allow you to repeat
# the entirety of the list an integer number of times. See the below examples:
small_list = [1]
# print(small_list*100)
small_list *= 50
# print(small_list)

# Clearly, there are many ways to add elements to lists and it is good to understand how they all work. In practice, you
# will actually use all of them frequently, so please get to using them!
########################################################################################################################
# Part III: Removing elements from a list
# Using lists is about controlling the data they hold, so it is also useful to know how to remove data elements from them.
# There are three main ways to delete elements from a list:

# Method 1: Deleting all elements with .clear()/[]
# The simplest case of removal is completely deleting the list's elements. There are two ways to do this in python, using
# the .clear() method and setting the list equal to empty brackets "[]". Given what you know about list sizes and the
# len() function, what do you expect the following code to produce:

need_to_empty = [1]*10000
# print(len(need_to_empty))
need_to_empty.clear()
# print(len(need_to_empty))

need_to_empty = [1]*10000
# print(len(need_to_empty))
need_to_empty = []
# print(len(need_to_empty))

# Method 2: Removing a specific element with the .pop() method
# If you need to remove a specific element from a list, the .pop() method can be used. It takes an element index as an
# argument, removes it and shifts every element behind it over, decreasing the size of the list by 1. In programming,
# counting starts at 0, that is, the first element in a list has index 1 and the nth has index n-1 (more on this in part
# III). Either way, below are some examples:
kill_first_entry = [1,2,3,4,5]
kill_first_entry.pop(0)
#print(kill_first_entry)
kill_second_entry = [1,2,3,4,5]
kill_second_entry.pop(1)
# print(kill_second_entry)

# Method 3: Removing all instances of an value with the .remove() method
# If you want to remove all copies of a specific value, you should use the .remove() method. It goes through the list and
# removes every element that is equal to the specified removal value. This method is especially useful if you have a list
# of strings and want to remove specific strings. Below is an example:

many_letters = ["A","B","C","A","B","C","A","B","C","A","B","C"]
# print(len(many_letters))
many_letters.remove("A")
many_letters.remove("B")
# print(len(many_letters))

########################################################################################################################
# Part IV: Accessing elements in a list
# Now that you know how to add and remove data from a list, it is time to cover element access in python lists. As mentioned
# before, the counting of elements in lists starts at 0. For an example, see below:

index_list =     [1,2,3,4,5]
# element index   0,1,2,3,4

# This important for element access as the format is list[index], which makes use of the bracket operator "[]". Below is
# an example of list element access:

# print(index_list[0])

# Becuase the size of a list often changes, python lists also support negative indexing. That is, to get the last element
# in a list, instead of putting in len(list) - 1, you can simply write "-1". This is especially useful if you are going to be
# changing the list's size:

# print(index_list[-1])
index_list.append(10)
# print(index_list[-1])

# Lastly, its important to know that you can "slice" lists by using a colon in the bracket operator. The result is a smaller
# list made up of the selected elements from the bigger list. The general syntax is [begin:end] although if you leave
# either blank, the begin is assumed to be 0 and the end is assume to be len(list) - 1. Below are some examples of how this
# works:

slice_list = [1,2,3,4,5]

# printing second element on
# print(slice_list[1:])

# printing first element to one less than the last
# print(slice_list[:-2])

# printing second and third elements
print(slice_list[1:3])

########################################################################################################################
# Part V: The "in" statement and similarities to strings
# It is often very useful to check if an element is in an a list, which is done with the the "in" statement. The statement
# has the syntax ELEMENT in LIST and returns a boolean. From this, it is very useful for if statements:

small_list = [0]

if 1 in small_list:
    pass
else:
    small_list.append(1)

# Lastly, a little connection between lists and strings can be drawn. It turns out that in python, strings are essentially
# lists of one string elements. Due to this, the [] operator also works for strings. Strings will be revisited in the
# future, but it is very useful to know how to use the [] operator. What do you think the following will print?

str1 = "strings are just like lists!"
# print(str1[0])
# print(str1[:-20])

########################################################################################################################
# Homework
# (T/F) python lists are indexed from 0
# (T/F) in python, you can put lists inside of lists
# You have a list of all the students at UNL, but want to remove anyone with your name. Given the list "unl_students"
# below, how would you do this?
unl_students = [] # assume this is a real list

# Create a list with the sequence [1,2,3] repeated 100 times. Print the initial list size, then remove all 2's and
# print the list size again.

# Print out the type of the first element in the below list:
hw_list = ["A", "B", "C"]

# Bug busters. What is wrong with the following code? How would you fix it?
long_list = [1]*1000
last_index = len(long_list) - 1
long_list.pop(-1)
# print(long_list[last_index])

# Challenge problem: Write code that creates a mathematical matrix of dimension 10x10 with every element equal to 10.