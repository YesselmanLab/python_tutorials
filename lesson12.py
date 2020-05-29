# Welcome to the twelfth lesson in the Yesselman Group's Python series
# Topics covered: Maninpulating Data with Pandas
########################################################################################################################
# Part I: Intro to Pandas and Setup
# Pandas is a very popular python module for manipulating and analyzing large datasets. It is consistently one of the most
# downloaded modules and is commonly used in science. Pandas owes much of its popularity to:

# 1. Its intuitive file input/output system
# 2. Dictionary-like syntax for element access and storage in dataframes
# 3. Strong compatibility with matplotlib
# 4. Easy filtration and conditional ordering of data

# ...among many other strengths!

# Clearly there are a lot of reasons to use Pandas, but first you need to get in installed on your current system. Below
# is the standard import statement:

import pandas as pd

# To check if you have pandas, try running this script from the commmandline. If the module is not imported, it can be 
# downloaded through pip ("pip install pandas --user") or through conda if you are using a virtual environment ("conda install pandas").
# Additionally, pandas needs numpy (numerical python) to run. If numpy is not already installed, repeat the above steps 
# for numpy. 

# With these steps completed, there are a few definitions to cover before moving on:

# CSV (or csv, .csv): a generic plaintext file format in which data is separted by commas, with column names in the first row
# and values in the lower rows

########################################################################################################################
# Part II: DataFrame Basics
# DataFrames are the functional backbone of pandas, serving as a highly tactile data holder. Consider the below data:

# name, height, age
# Jeff, 1.65,10
# Kimmy, 1.50, 13
# Michael, 1.70,15
# Molly, 0.80, 8

# For this kind of grouping, all of the data in each row is related and correspond to the same entry or object (in this case,
# probably a person). This can also be though of as a dictionary where the keys are column names and the values are lists. In 
# turn, this can be quickly converted into a DataFrame. See the below example:

raw_data = {
    "name" : ["Jeff", "Kimmy", "Michael","Molly"],
    "height" : [1.65,1.50,1.70,0.80],
    "age" : [10,13,15,8]
}

df = pd.DataFrame(raw_data)

#print(raw_data)
#print(df)

# Uncomment the above lines and note the difference between the simple dictionary and the DataFrame. The improved printing of
# data is just one of the many advantages of using DataFrames. Additionally, you can see the first and last n entries in a 
# DataFrame with .head() and .tail(), respectively. See the below example:

#print(df.head(2))
#print(df.tail(2))

# Now is a good time to cover some more pandas terminology. In general, a DataFrame represents a table similar to what you might
# have encountered in a spreadsheet program like Microsoft Excel, and more specifically a pivot table. This means that there are 
# "columns" holding all the data of a specific type, and each "row" has a number and represents the collection of each item in 
# the ith position of each column, all grouped together. Similar to dictionaries, a "for loop" applied directly to a dataframe 
# will iterate through the column names of the dataframe (see below). To access a specific row, the method .loc() can be used, 
# which is supplied with an index (though .loc() can be supplied with other arguments as well).

#for col in df:
#    print(col)

#print(df.loc[0])

# To access a single data series in a dataframe, you can use the brackets operators "[]", as with dictionaries. This in turn gives
# access to the associated data series. Likewise, more columns can be added using the brackets operator. See below:

#print(df)

df["favorite_color"] = ["red","blue","blacK","purple"]

#print(df)
########################################################################################################################
# Part III: File IO With Pandas
# As mentioned before, one of the strengths of Pandas is its built-in ability to read and write from files. Reading data
# in can be done with the .read_csv() method, which takes the file path to a .csv file. See the example below:

animal_df = pd.read_csv("data/animals.csv")

#print(animal_df)

# That was easy right? In addition, if a data entry's string can easily be converted to a a number, the conversion will be
# done automatically. Note that this is not true for lists, i.e. if each entry in a column is itself a list. This is 
# illustrated below:

# print(type(animal_df["uniq_id"][0]))

# While this is a slightly different type (numpy.int vs int), it still operates like a normal int elsewhere in python. 
# Alternatively, data can be imported with methods like .read_excel(), which takes the file path to a .xlsx file. There
# are many other .read_XX() methods which allow importing of data to a DataFrame and this further highlights the built-in
# file input methods that come with pandas.

# On the flip side, saving a DataFrame to a .csv file can be done with .to_csv(), which takes the output .csv file as an
# argument. When doing this, it is a good idea to use the keyword "index" as shown below to avoid having the entries' index
# number also written as a column:

# animal_df.to_csv("output.csv",index=False)

# It is important to remember that if the entries in the series are a more complex dataype than a str(), int() or float(),
# a difficult to parse string will be placed in the output .csv. To confront this, it is a good idea to convert structures
# like lists or dictionaries to a custom string format and to develop functions to read/write from these formats.
########################################################################################################################
# Part IV: Basic DataFrame Manipulation: Slicing and Sorting
#

