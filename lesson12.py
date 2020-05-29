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

# df: short for DataFrame (see definition below), often used at the end of a variable name to indicate that it is a pandas
# DataFrame object or something similar

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
# The power of manipulating pandas dataframes is that choices made in the column space propagate into the row space and 
# individual groupings of data can be moved around or removed in tandem. Two of the most common DataFrame manipulations 
# are to slice (or filter) and Sort. On the slicing front, there are a handful  of common use cases:

# 1. Only keeping desired columns:
# The general format is SLICED_DF = ORIG_DF[['col_name1','col_name2',...]]
names_only = animal_df[['animal',"uniq_id"]]
#print(names_only)

# 2. Only keeping desired rows:
# To slice by rows, you can make use of the .loc[] method, which can take a list of integers as input. Below is a simple 
# example of this
select_rows = animal_df.loc[[0,1,2,3]]
#print(select_rows)

# 3. Conditionally keeping desired rows:
# This is similar to the method shown in #1 above. Here virtually any logic can be used to slice the data, but notice that
# the synatx is a little different. Instead of 'and'/'or', the operators '&'/'|' are used, and each boolean statement
# should be surrounded in parantheses, as seen below:

lions_and_tigers = animal_df[(animal_df["animal"] == "tiger") | (animal_df["animal"] == "lion")]
# print(lions_and_tigers)

# Sorting is definitely more nuanced than slicing, and some common examples are shown below:

# 1. Sorting by a single column's values
# This is done with the .sort_values() method. This method is driven by the "by" argument, which is set equal to the column(s) 
# that will be used for row sorting. It is possible to use multiple column names, but that will be covered in the next item. In 
# both instances, however, the column names must be presented as a list of strings.  Here, it is a good idea to use the key
# word argument "inplace", which specifies whether or not the existing dataframe will be altered or if a new one will be made.
# Consider the below example:

#print(animal_df)
animal_df.sort_values(by=["animal"],inplace=True)
#print(animal_df)

# 2. Sorting by multiple column valuees
# As with item 1 above, this is achieved with the .sort_values() method, but instead multiple items are included in the "by" 
# variable assignment. It should be noted that they will be sorted in the order they are lists. That is, in the below example,
# the entries will be sorted by animal identity, then within each animal, they will be sorted by the values in the "water_need"
# column.

#print(animal_df)
animal_df.sort_values(by=["animal","water_need"],inplace=True)
#print(animal_df)
########################################################################################################################
# Part V: Using Pandas with matplotlib

# Pandas is also extremely powerful when combined with matplotlib to produce plots. Conside the below example:
import matplotlib.pyplot as plt


# Another powerful aspect of Pandas is how well it meshes with matplotlib for plotting. Similar to dictionaries, pandas
# dataframes associatively store information, and this can be leveraged when plotting data. Consider the below code and how 
# little has to be done to plot a significant amount of data. While this is a single example of how to use pandas and matplotlib,
# using pandas for plotting is something that you will get better at as you use it more.

df = pd.read_csv("data/graphing_data.csv")

# loading the data into the chart
for col in df:
    if col != 'x':
        plt.plot(df['x'],df[col],label=col)

# annotating the chart
plt.xlabel('x')
plt.ylabel('y')
plt.title('pandas is great for plotting!')
plt.legend()
#plt.show()
########################################################################################################################
# Part VI: Moving forward with Pandas

# Clearly you can do a lot with pandas, but in this tutorial we only just scratched the surface. As before, the best way 
# to improve your skills and get things accomplished are to use the documenation for pandas (https://pandas.pydata.org/docs/user_guide/index.html#user-guide)
# and to use websites like StackOverflow or whatever else you can find on google!
########################################################################################################################
# Homework
# (T/F) A csv has to have column names.
# (T/F) Pandas makes file input/output quick and deals with data conversion automatically.


# Make a dataframe from the data/graphing_data.csv file and only keep the rows where x >= 0.


# Add a new Series to dataframe called tangent, which is equivalent to y = tan(x)


# Chart the data contanied with the DataFrame as was done above in Part V.


# Make a dataframe from the data/students.csv file and sort the entries by name. Save the .csv as data/students_alphabetical.csv


# Make a dataframe from the recently created data/students_alphabetical.csv file and plot the scores as a plt.hist(). Next, filter out
# scores lower than 80 and make another plot
