# Welcome to the sixth lesson in the Yesselman Group's Python series
# Topics covered: sets, review of strings
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
# Part II: Adding more to strings
# String maninpulation is an extremely important part of programming and data analysis as information is often outputted to 
# a string from other applications. The first method to cover is called .split(). In the paranthesis, you put a delimiter
# (though they are whitespace by default) and then a list of the broken up strings is produced. Consider the following code:
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

# To see if a string contains a substring, you can make use of .find(). This method takes a substring as an argument and 
# returns the index that the desired substring begins at, else -1 if the string does not contain that index. Below are
# are some examples:

big_string = "first_second_third"

# print(big_string.find("second"))
# print(big_string.find("fourth"))

def is_rna_strand(input_sequence):
  """Method that checks if the input sequence is RNA (has U) or not"""
  if input_sequence.find("U") != -1:
    return True
  else:
    return False

# Lastly, you can change the case of a string with .upper() and .lower(). This can be helpful to avoid annoying case-related issues

def name_in_class(input_name, input_class):
  """Method that checks if a student's name is in a class"""
  # first, change the name to lower case
  student_name = input_name.lower()
  # now loop through each name in the input class 
  for candidate in input_class:
    # see if the candidate name contains the student name
    if candidate.lower().find(student_name) != -1:
      return True
  # if we get through the entire class and it's not true, return False
  return False


# Miscellaneous examples:
# Below are some miscellaneous examples of how to use sets and some of these more advanced string methods()

def check_unique_scores(score_list):
  """Method that checks if the scores presented are unique. Returns true if only unique, false if there are duplicates"""
  return len(score_list) == len(set(score_list))

def summarize_names(name_list):
  """Method that takes list of names as input and prints out a basic summary"""
  unique_name_list = set(name_list)
  for name in unique_name_list:
    print("Name: {}\tOccurences: {}".format(name,name_list.count(name)))
  print("Total names: {}\tTotal People: {}".format(len(unique_name_list),len(name_list)))
  
def string_to_values(input_string):
  """Method that takes a string of '|'-delimited values and converts them to a list of values."""
  value_list = []
  for token in input_string.split('|'):
    value_list.append(float(token))
  return value_list

def values_to_string(input_values):
  """Method that takes a list of values and converts them to a '|'-delimted string"""
  token_list = []
  for value in input_values:
    token_list.append(str(value))
  return '|'.join(token_list)

########################################################################################################################
# Homework
# (T/F) For a list L, len(L) < len(set(L))
# (T/F) BASE.find(SUBSTRING) returns the index at which SUBSTRING begins in BASE or -1 if SUBSTRING is not in BASE
# (T/F) "1 2 3 4 5".split() returns a list of integers

# What is main advantage of using a set over a list?

# How do you add an item to a set and then check if that item is in the set? How is this different than for strings?

# Do .lower() and .upper() impact non-alphabetic characters? If so, how? 

# For a list with N strings, when join is called, how many times is the joining string added to the output string? 

# Bug Busters.
# Jim is trying to find the max number from the following string but is not getting the right answer. While he wants 
# 500, the supplied answer is 4. What is he doing wrong?
numbers = "01 2 3 4 00500 -1".split()
max(numbers)

def item_count(input_list,input_item):
  pass
# create a function that tells how many times 'input_item' is found in 'input_list'. Make sure your implementation makes
# use of set()

def long_A_stretch(input_sequence):
  pass
# create a function that can tell if there is a continuous stretch of 20+ A's in the supplied sequence

def parse_values(value_string):
  pass
# create a function that takes a string as follows "1|2|3|4|5", and returns a list of floats. Additionally, if a value is
# negative, set it to 0

def thresholding_entries(entry_list,threshold):
  pass
# create a function that returns a list of entries whose occurrence >= threshold. I.e., for input list [1,2,3,4,4,4] and
# threshold = 2, the answer would be [4]. 
