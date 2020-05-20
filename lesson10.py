# Welcome to the tenth lesson in the Yesselman Group's Python series
# Topics covered: Unittesting and Docstrings
########################################################################################################################
# Part I: What is unittesting? Why use it?
# Now that you can write classes and functions and store them in .py files, you can also start to build larger projects 
# and distribute this source code all over the place. But with great power comes great responsibility. You need to ensure
# your code works as desired and that it works on the platform on which it is being used. In fact ensuring that code 
# functions properly is one of most important parts of programming. 

# In python, this issue is addresed with unittesting, which is the process of breaking down the code's functionality into
# manageable units and then ensuring that all of the  units both function as desired AND don't have unintended side
# effects/behavior. From here on in the words "test", "testing file" or  "Unittest" will be used interchangeably in 
# reference to a python file containing a code that tests a "unit" of other code. Ultimately, the goal is to create a 
# set of python files that test the functionality of your project's code units.
########################################################################################################################
# Part II: Writing Unittests in Python
# In this section we will be looking at some example unittests for the Atom class found in atom.py and how unittests are
# generally written.

# The first part of a unittest file are the import statements. Here, the code to be tested will be imported as well as 
# any companion modules that may be needed and of course, the unittest module.

# the code being tested
import atom 
# the unittest module itself
import unittest 
# companion modules that will be needed (don't worry if you don't know what numpy is, it will be covered in another lesson)
import numpy as np

# With the neccessary code imported, the Unittest class is declared. In general, you will be testing functions and classes
# that you write. Each class will correspond to a Unittest Class used to test the class itself (class Atom in this case). 
# For functions, it often makes sense to either group them with an existing class (if they are similar to/invovled with
# that class) or to group all free functions together into a single Unittest class. Regardless, a good format for the name
# of the unittest is class [ORIGNALCLASS]Unittest(unittest.TestCase)
# Note that the "unittest.TestCase" inside of parantheses is needed at the end of the class declaration for the unittest 
# framework to function properly. 
# Additionally, you will notice that there is a triple quoted (""" """) string below the class declaration. This is a docstring
# and it gives python information about the class which is shown if a test fails. ( See more here https://www.python.org/dev/peps/pep-0257/).
# Normally, these docstrings can be accessed through the help() function. For example, to view the docstring of the Atom
# class, you could type help(atom.Atom). You will need to write your own docstrings when making unittests (or code for that
# matter), and you should focus on describing what is going on in that class/method/function/

class AtomUnittest(unittest.TestCase):
    """Unit tests for the Atom Class from atom.py"""
# With the class created, the actual test cases can be written. For a test to get called when the unittests are run, the method
# has to be named "test_SOMETHING", as shown below. Then, within each method, a variety of assertions are made, with the syntax
# self.assertTYPE, where TYPE is a variety of existing assertion methods (you can read more about all of them here https://docs.python.org/3/library/unittest.html)
# To see how they work, try running this file and see what is output from the test_basic() method below
    
    def test_basic(self):
        """Example of a unittest"""
        self.assertTrue(True)
        self.assertTrue(False)

# When actually testing the class, there should roughly be one test method for each actual method. This is not a hard rule, but 
# it is a good rule of thumb. Notice that each method has a docstring describing its function and what it tests.

    def test_creation(self):
        """Testing the default and copy constructors"""
        target_string = "H1 1 2 3"
        first = atom.Atom("H1",np.array([1,2,3]))
        second = first.copy()
        self.assertTrue(target_string == str(first))
        self.assertTrue(target_string == str(second))
        
    def test_move(self):
        """Testing that Atom.move() functions properly """
        test_atom = atom.Atom("TEST", np.array([0,0,0]))
        test_atom.move([1,2,3])

# .assertListEqual() is an example of a more complex assertion that compares two lists

        self.assertListEqual(list(test_atom.coords),[1,2,3])
        
        test_atom.move([-3,-3,-3])
        self.assertListEqual(list(test_atom.coords),[-2,-1,0])
    
    def test_repr_str_equivalent(self):
        """Testing that the __str__() and __repr__() methods produce equivalent, correct output"""
        target_string = "TEST -1000 0 1000"
        test_atom = atom.Atom("TEST",np.array([-1000,0,1000]))
        
        self.assertEqual(target_string,str(test_atom))
        self.assertEqual(str(test_atom),test_atom.__repr__())

# Lastly, for a set of unittests to work, the below code is needed. It can be copy and pasted diretly, but it plays off of how
# python has special variables for each script. __name__ is an example of one and it can have different names depending on 
# how the .py file is being called. __name__ == "__main__" tests if the file is being called directly and not being imported 
# into another .py file. 

if __name__ == '__main__':
    unittest.main()

########################################################################################################################
# Part III: Best practices and using Docstrings
# Above is a quick and dirty example of what a unittest should look like. In the interest of keeping this lesson file 
# brief, not many test cases were shown, so it is important to also cover some best practices when designing unittests:
    
    # 1. Make sure to test all of a class/function's functionality. This one is pretty simple: you need to make sure that
    # all of the functionality the code provides is directly tested. In practice, this means that when a function is 
    # updated or new ones are added, the unittests ALSO need to be updated.

    # 2. Think about the major cases you will be working with and make sure they are all addresssed. It is common for
    # code's behavior to be subject to different ranges of values/parameters and be constant within those ranges. Take
    # the example of a square root function. There are 3 major regions of input values -> input < 0, input >= 0 and 
    # input < 1, input >1. Within each of these regions there should be distinct behavior, so it is important to sample
    # each of the three ranges. Always think about what outputs should be for your code and design your unittests around
    # them. 

    # 3. Know what each self.assert statement you use does. The behavior of the various self.assert types can be counter-intuitive
    # at times. For example, self.assertFalse notoriously allows values like 0, "", [] and None which are considered 
    # to be "Falsy" (https://stackoverflow.com/questions/35038519/python-unittest-successfully-asserts-none-is-false). 
    # If you are using a new assert method you are not familiar with, you should read up on how the method operates
    # under the hood.

    # 4. Target edge cases. As a follow-up to Rule 2 above, focus on the boundaries of your code's functional ranges. 
    # These are typically areas where problems show up, so make sure you understand how the code performs in these 
    # regions. Calling back to the square root example, it would make sense to see how values like 0 and 1 are impacted. 

    # 5. When writing important and/or complicated code, consider setting up the unittests for the desired behavior
    # BEFORE you write the code. At the end of the day, it's important to remember that coding is not an end, but 
    # a means to an end. In the Yesselman Group, you will be trying to solve RNA-related problems with code, not just
    # write a bunch of code. Ultimately, if the code correctly transforms data in the desired manner, you have succeeded!
    # Building unittests before writing the code allows for efficient and effective creation of code. 

    # 6. Make good docstrings. In general, docstrings are really important to writing good python code. When making a 
    # docstring, you should try to focus on providing supplemental information not made clear by the function/class/variable
    # names visible to the code user. 

# As a quick recap, writing unittests is an extremely important part of creating code. These tests are at the corner
# of ensuring code works and can be trusted. Often, when someone else uses your code, the first thing they will do 
# is run the unittests as this can provide some security that the code is working on their own machine.
########################################################################################################################
# Homework
# (T/F) Code generally performs the same regardless of inputs, so specific regions should not be targeted.
# (T/F) Unittests are a good way to ensure code works as desired and does not contain bugs.

# What are docstrings supposed to do and why do they matter for unittests?

# Create a file called rna_unittests.py that tests the RNA class you have been working on the past few weeks. Make sure
# that you:

    # -make a test for every major functionality of the class
    # -target the edge cases for each method
    # -have good docstrings

