# Welcome to the sixth lesson in the Yesselman Group's Python series
# Topics covered: dictionaries
########################################################################################################################G
# Part I: Dictionary Basics
# As explored in the previous lesson, sets are a type of "associative" container, roughly meaning they store unique values
# only. While sets are useful, dictionaries allow you to additionally associate something with that unique value. In python,
# these unique values are referred to as "keys" and the associated object is a "value", together, they form "key-value" pairs.
# Dictionaries are extremely useful as they can store large amounts of information in a digestable manner that is easy 
# for us mere humans to comprehend. This is largely due to dictionaries' ability to handle nested data structures, which 
# closely reflect how data exists in real life, unlike lists, which are often confusing for for representing more complex
# data structures. That being said, dictionaries are ultimately just sets of key-value pairs! Below is an example of a dictionary
# literal declaration:

my_dict = {
        "A" : 1,
        "B" : 2,
        "C" : 3
        }

# The general dictionary declaration format is as follows:
# DICTIONARY = {
#   KEY1 : VALUE1,
#   KEY2 : VALUE2,
#   KEY3 : VALUE3,
#       ... }
# Not that keys have to be "immutable" (unchangeable) types. For now, this just means that they must be strings, integers
# booleans, or floats. Values can be anything though, including lists or other dictionaries! Below are some more advanced
# declaration examples

rnas = {
    "sequence" : [],
    "structure" : [],
    "energy" : [],
    "fold_flag" : []
        }

school_class = {
        "students" : [
            {
                "name" : "Joe",
                "major" : "biophysic"
                }
            ],
        "teacher" : {
            "name" : "Rhiju" 
            }
        }

########################################################################################################################
# Part II: Using the "[]" and "in" operators
# Just like with lists, dictionaries can be manipulated with the brackets operator. They can be used to do three things:
# 1. Access existing value
#       print(my_dict["A"])
# 2. Re-assign existing value
#       my_dict["A"] = 10
#       print(my_dict["A"])
# 3. Add NEW key-value pair to the dict <= unique to dicts()
#       my_dict["D"] = -1
#       print(my_dict["D"])

# When accessing an element, you can also use the value's supported methods. Just consider that the DICTIONARY[KEY] gets
# replaced with the key it corresponds to. Consider the below example:

list_dict = {
        "list" : []
        }
# print(list_dict["list"])
for new_num in range(10):
    list_dict["list"].append(new_num)
# print(list_dict["list"])
list_dict["list"] *= 10
# print(list_dict)

# As with sets and lists, dicts support the "in" operator. For this data structure, it is often important to make sure
# you aren't overwriting an existing value. Consider the following function that tells how many time each letter appears 
# in a string:

test_sentence = "This is a test sentence to see how many times each letter appears in the sentence"

def make_content_dict(input_string):
    """Method that takes an input string and returns a dict with characters as keys and occurrences as values"""
    frequency_dict = dict()
    for character in input_string:
        if character not in frequency_dict:
            frequency_dict[character] = 1
        else:
            frequency_dict[character] += 1
    return frequency_dict

str_dict = make_content_dict(test_sentence)
#print(str_dict)
########################################################################################################################
# Part III: Iterating through dicts
# Without knowing all of the keys in a dict, using a for loop is the only way to visit all key value pairs. By default, 
# the for loop iterates through the dict's keys. See the below example:
demo = {
    "KEY1" : 1, "KEY2" : 2, "KEY3" : 3, "KEY4" : 4
        }

def explore_keys(input_dict):
    """Method that shows the keys in a dictionary"""
    for key in input_dict:
        print(key)

# explore_keys(demo)
# While you can still access the dict's values with the current key in the for loop, you can explicitly access the object's
# keys or values with the .keys() and .values() methods, respectively.

def explore_keys_and_values(input_dict):
    """Method that shows the keys and values in a dictionary"""
    for key in input_dict.keys():
        print(key)
    for value in input_dict.values():
        print(value)

# explore_keys_and_values(demo)

# Still, sometimes you will want to iterate through both keys and values in dictionary at the same time. This can be achieved
# easily with .items(). See an example below using this method:

# for key, value in demo.items():
#    print("{} : {}".format(key,value))

########################################################################################################################
# Part IV: More Examples
# Below are some more examples using dictionaries. Investigate these functions closely, they may (or may not) be related
# to the homework problems below!

def key_in_dict(input_dict, input_key):
    """Method that checks if a key is in a dict. Returns a bool"""
    return input_key in input_dict

def sort_student_score(name_list, score_list):
    """Method that takes a list of names and scores and returns a dict with keys as letter grades and a list of names as as values"""
    score_dict = {}
    for grade in "A B C D F".split():
        score_dict[grade] = []

    for name, score in zip(name_list, score_list):
        if score >= 90:
            score_dict["A"].append(name)
        elif score >= 80:
            score_dict["B"].append(name)
        elif score >= 70:
            score_dict["C"].append(name)
        elif score >= 60:
            score_dict["D"].append(name)
        else:
            score_dict["F"].append(name)
    return score_dict

def get_bp_content(input_sequence):
    """Method that takes an input_sequence string and returns a dictionary of normalized bp content"""
    total_nts = len(input_sequence)
    bp_content = {}
    for nt in input_sequence:
        if nt not in bp_content:
            bp_content[nt] = 1.
        else:
            bp_content[nt] += 1.

    for bp in bp_content.keys():
        bp_content[bp] /= float(total_nts)
    return bp_content
########################################################################################################################
# Homeowrk
# (T/F) Dictionaries are associative containers.
# (T/F) Dictionaries can have identical keys.
# (T/F) A for loop automatically iterates through a dictionary's values

# Bug Busters
# Cassie wants to make a function that takes a list of numbers and keeps track of how many times each occurs. What's wrong 
# with the code? 

def occurence_dict(int_list):
    """Method that takes a list of ints and returns a dict with keys as integers and values as occurrences"""
    freq_dict = {}
    for num in int_list:
        freq_dict[num] = 1
    return freq_dict

# Easy problem
# Make a function that takes an input dict and prints the dicts values() to the screen
def print_values(input_dict):
    pass

# Medium problem
# Make a function that takes a list of integers and places them into a dictionary with the following format:
# output_dict = {
# "even" : [list of even numbers], "odd" : [list of odd numbers] }

def even_odd_dict(integer_list):
    pass


# Hard problem
# Make a function that takes two dicts and merges them together. You can assume they have the same keys:
# Example input/output
# input
dict_1 = {"A" : [1,2,3,4]}
dict_2 = {"A" : [5,6,7,8]}
# output
output = {"A" : [1,2,3,4,5,6,7,8]} # or [5,6,7,8,1,2,3,4], order doesn't matter

def merge_dicts(dict_1, dict_2):
    pass
