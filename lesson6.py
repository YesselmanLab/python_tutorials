# Welcome to the sixth lesson in the Yesselman Group's Python series
# Topics covered: sets, review of strings/iteration
########################################################################################################################
# Part I: sets
# In programming, a container object is something that holds other types of data and usually has no intrinsic properties
# iteself. Previously we have covered lists, but today we will be talking about sets, which are a type of a associative
# container, which just means that element storage is dependendent on the element's identity. That may sound confusing, 
# but all it means is that a set stores a unique list of objects. Consider the example below and call show_container_contents
# on both the list and set below. What are the outputs? 

my_nums = [10]*100 + [20]*100 + [30]*100
num_set = set(my_nums)

def show_container_contents(input_container):
  for element in input_container:
    print(element) 
# When you want to declare a set, the easiest way is a literal declaration with braces. Below are some examples:
my_set = {
1,2,3,4,5
}
string_set = {
"A","B","C"
}
# Unlike lists that use the .append() method, you used .add() to add to a list, as follows:
string_set.add("D")

# additionally there are .clear() and .remove() methods as with lists. See the example below that clears a set:


def clear_set(input_set):
"""Method that clears a set and shows size before and after"""
  print("Size before clearing {}".format(len(input_set)))
  input_set.clear()
  print("Size after clearing {}".format(len(input_set)))

# Sets are very useful for analyzing large data sets as you can easily see all types of an entry. Below are some 
# examples of using sets:

class_scores = [90,93,95,80,94,90,49,93,87,95]

def get_unique_scores(score_list):
"""Method that gets the unique scores from a set of test scores"""
  score_set = set(score_list)
  print("There are {} unique scores in this list".format(len(score_set)))

def is_lucky_number(input_number):
"""Method that checks if an input number is a lucky number."""
  lucky_number_list = {1, 3, 7, 9, 13, 15}
  if input_number in lucky_number_list:
    print("{} is a lucky number".format(input_number))
  else:
    print("{} is not a lucky number".format(input_number))

########################################################################################################################
# Part II: Adding more to strings/iterations
# String maninpulation is an extremely important part of programming and data analysis as data is often outputted to 
# a string from other applications. The first method to cover is called .split(). In the paranthesis, you put a delimiter
# (though they are spaces by default) and then a list of the broken up strings is produced. Consider the following code:
raw_data = "1 2 3 4 5"
strings = raw_data.split()
# for tk in strings:
#   print(tk)
# What does the above code do? Given what was discussed above, below is a splitting of some comma-separated data
comma_separated = "10,9,8,7,6,5,4,3,2,1"
data_tokens = comma_separated.split(",")
#print(len(data_tokens))

# The reverse of .split() is .join(). It is called in the following manner: DELIMITER.join([STRING_LIST]). Consider the 
# example below:
my_strings = ["first","second","third","fourth"]
connected = ",".join(my_strings)
#print(connected)
