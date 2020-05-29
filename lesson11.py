# Welcome to the eleventh lesson in the Yesselman Group's Python series
# Topics covered: Using Matplotlib for Data Visualization
########################################################################################################################
# Part I: The Importance of Visualizing Data (in Python)
# Data Visualization is the process of taking numerical data and converting into a visually digestible format like a 
# graph or chart. You more than likely have some experience doing this already in Microsoft Excel, but its still worth 
# noting the advantages of visualizing data:
# 1. Allows you to easily identify trends
# 2. Charts are information dense and efficiently respresent large amounts of data
# 3. Properly-visualized data can effectively convey a story or support an argument
# 4. Makes data and trends easy to communicate to others
#           ... and many more!

# Python specifically is well suited for data visualziation given and has the following general advantages:
# 1. Significantly faster than Excel and other spreadsheet applications
# 2. Can handle very large datasets
# 3. Saving charts/figures/graphs is easy
# 4. Python's object oriented paradigm gives the user significant control over chart formatting
# 5. Built-in data structurs like list(), set() and dict() are convenient for grouping data
# 6. There are a variety of open-source, free-to-use modules like matplotlib, seaborn and more
#           ... and many more!

# Clearly, there are many reasons to use visualization methods AND do this visualization in Python. From here on in, this
# tutorial will focus on using matplotlib, the most widely-used graphing module. While other modules may be better 
# for specific projects, matplotlib is a great general purpose library. Additionally, many other modules are built on
# top of matplotlib, so any knowledge gained here will likely translate to those modules as well. 

# To get started with matplotlib, use the below import statement:
import matplotlib.pyplot as plt
# It is highly recommended you import this module EXACTLY as shown above. This is the standard convention in python and
# there aren't any great reasons to not follow the convention, so this is a time to just go with the flow :)
# The matplotlib library may not be installed on your machine. If this is the case, there are two main options for getting
# the module working directly:

# 1. Get it directly installed onto your computer. For this method, try the command "pip install matplotlib --user" on 
# the commandline. There is a chance you will have to install other packages for this to work, which will be indicated
# in the terminal.

# 2. Install it into PyCharm. To do so, go to settings > Project Interpreter click the "+" symbol in the bottom left 
# corner. This will open a new window titled "Available Packages" where you will type "matplotlib" into the search bar.
# After selecting the module, click the "Install Package" button at the bottom of the page. 

# With the module installed, we can get on to actually making graphs! 
########################################################################################################################
# Part II: Scatter Plots
# Below is an example of how you could make a scatter plot with matplotlib. The main prerequisite for this type of plot
# are two list()'s holding only numbers, having dimensions 1xN  and of the same length N.
x_values = range(-50,51)
y_values = [x*x for x in x_values]

# the .scatter() method is used to give a set of values to the chart and requires x and y arguments
plt.scatter(x_values,y_values)
#plt.scatter(range(-50,51),range(101))

# this plot would be somewhat plain without anything else, so more detail can be added to the plot with 
# the below methods. If it is unclear what any of them do, change them and feel free to see what they do!
plt.xlabel("x")
plt.ylabel("y")
plt.title("an example scatter plot")

# to actually see the plot, you need the .show() method. Uncomment the below line and run this script to see what happens
#plt.show()

# if instead you would like to save the plot as a file, you can call .savefig(), which takes the .png filename as a path. # Note that other extensions can be used, but they must be legitmiate image formats like .pdf, etc
#plt.savefig("lesson11scatter.png")

# the last method that always needs to be called is the .clf() method. This is because there is only one "plt" object at a
# time in python and if you didn't clear it out, everything would just be stacked on top. On the other hand, this can 
# be used to your advantage to show multiple data sets. For every set of data, a separate scatter() call must be made. To
# see an example of this, uncomment line 53 and rerun the script.
plt.clf()

########################################################################################################################
# Part III: Line Plots
# Line plots are identical to scatters in terms of data requirements and calling convention, with the only difference 
# being that all the data points are connected by the order in which they are added, it is usually much slower than using
# a scatter plot, and the x values are actually optional. Regradless, below is the annotated code for a sample line plot:

# creating the initial data ranges
x_values = range(100)
y_values = [x/2 + 20 for x in x_values]

# inserting the plot values into the plot() and setting the x/y labels as well as the title. Note that if desired, only
# the y values need to be given to the plot() method
plt.plot(y_values)
plt.xlabel("x")
plt.ylabel("y")
plt.title("an example line plot")

# seeing the plot with .show()
#plt.show()
# though the option to use .savefig() is still there:
# plt.savefig("lesson11plot.png")
plt.clf()

# As before, uncomment line 88 to see how this looks.
########################################################################################################################
# Part IV: Histogram Plots
# A histogram plot is a different type of plot that shows frequency information about a dataset. Histograms take only
# a single 1xN list() and then show the frequency of the elements in the input list(). The xlabel,ylabel,title, etc 
# parts work as before, but this plot type is different than the previous ones in that it doesn't work always work very
# well out of the box. This is mainly due to the "binning" of the input values. By default, the bins are truncated integers,
# where 1.5 -> 1, 1.9 -> 1, etc. This can be overridden, but is usually not super simple.

values = [1.1,1.6,1.8,1,2,2,2,2,2,2,2,2,2.9,3,3,3,3,3,3.3,4,4,4.6,6,6,6,6,6.6,6.5,7.2]
# Same set up as before, except that only one array is needed as an input. If two are given, this will actually cause an 
# error. 
plt.hist(values)
plt.xlabel("value")
plt.ylabel("occurrence")
plt.title("example historgram plot")
#plt.show()
#plt.savefig("lesson11hist.png")
plt.clf()

########################################################################################################################
# Part IV: Hybrid Plots
# A powerful aspect of matplotlib is the ability to make hybrid plots where multiple types of plots are overlayed on top
# of eachother. For example, multiple sets of data could be overlaid as scatters with the average being a line plot. 
# Consider the below example where a dictionary of student's scores are plotted. This is a more realistic look at something
# you may do with matplotlib, so there are a few new features you have not seen yet. To see what the output plot looks
# like, uncomment line 150

score = {
    "Bjarne Stroustrup" : [80,90,95,100],
    "Herb Sutter" : [94,60,70,85],
    "Chandler Carruth" : [87,65,38,98],
    "Scott Meyers" : [70,80,90,100]
        }

averages = [0]*4

for name, scores in score.items():
    # a for loop can be used to add multiple data series to the plt via scatter(), plot(), hist(), etc
    plt.scatter(range(1,5),scores,label=name) 
    # here the keyword "label" specifies what the series will be named in the plot's legend. 
    
    for index, val in enumerate(scores):
        averages[index] += val

averages = [x/4 for x in averages]
# unlike the scatters above, a plot is used for the scores average
plt.plot(range(1,5),averages,label="all_students_average")

plt.xlabel("test_number")
plt.ylabel("score")
plt.title("cpp_expert_scores")
# the method legend() will create a legend in the plot with names for the data series, if applicable
plt.legend()
plt.show()
plt.clf()

# With hybrid plots, virtually anything is possible, but it is important to remember that there is only one plt object
# for these types of plots, so things like the xlabel and ylabel can only have one value.
########################################################################################################################
# Part V: Using kwargs and Reading the Docs
# Much of the power of matplotlib comes with the massive amount of customization available and the ease with which it 
# can be accessed. In this module, this is largely done through a variety of class methods and their associated key-word
# arguments or "kwargs". 
# A kwarg is a special feature of the plot (although it is used elsewhere as well) that can optionally specify something. 
# As seen above on line 135, the "label" keyword specifies what the data series is named and has the format label="NAME".
# Other kwargs that can be set include:
# 1. line width or marker size (for plots and scatters respectively)
# 2. marker/line color
# 3. the number of bins to be used in a histogram (or the size of the bins)
# 4. marker shape
#           ... and many, many more

# Additionally, an advantage of kwargs is that they can be put in any order (once the required arguments are supplied).
# For example, when making a plot, the following calls will give the same output:

plt.plot(range(4),label="TEST",color='r')
plt.plot(range(4),color='r',label="TEST")

plt.clf()

# That being said, not everything one could need/want to know about using matplotlib could be covered in a single lesson.
# There are a variety of other plot types available, including those with error bars and 3d plots. The important point
# here is that to get what you want done with matplotlib, you will likely need to read the documentation and look things
# up yourself. To do so, you can either go here (https://matplotlib.org/users/index.html), or just search what you want
# to do on the internet! An important part of becoming a better programmer is learning how to do things on your own, which# can be done by just searching what you need on the internet! Websites like StackOverFlow.com and github.com are also 
# good places to visit.
########################################################################################################################
# Homework
# (T/F) plt.plot() requires two lists() of data to print.
# (T/F) plt.clf() cleans out the plt object's current data. If plt.show() is called after this, it will show a blank box
# (T/F) The following is the correct convention: import matplotlib.pyplot as PLT

# Bug Busters
# Sarah is trying to make a scatter plot and is able to get her data to appear, but notices that there are also other 
# data on her plot. What can she do to fix this? Her code is below:

x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [x*(x%5) for x in x_values]

plt.scatter(x_values,y_values)
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("why is this plot so buggy?")
#plt.show()

# Extract the data from data/mystery.csv, which contains an x and y column. Read in the data and plot the x,y pairs on a 
# scatter plot. What does the plot produce? save the image

# Plot sine, cosine and tangent from -2pi to 2pi, making sure to label each function for the legend as well as the axes
# and a title. This should be a plt.plot(), not scatter.

# Using the randint() function from the random module, collect 10,000 data points bewtween 0 and 100, inclusive, and plot
# their frequencies using a plt.hist() plot. Make sure to label the axes and provide a title. How random are these random
# numbers?
