# here are some more more examples for looping
# Example 1: showing the progression of inner/outer incrementing for loops
# As we discussed, the inner loop has to fully cycle through its values before the outer loop moves on. 
# In this first demo, we will use the list with values [0,1,2,3,4].

values = range(5)

for outer in values:
    for inner in values:
        print("outer value: ", outer, " inner value: ",inner)

# Example 2: Every combination of rolls for two playing dice (duplicates included). For this one, we will be making a list of lists
# with dimensions N x 2, that is a list of smaller lists with size 2, just as below:
target_values = [
        [1,2],
        [3,4],
        [5,6]
        ]

# once the below code runs, make nested for loop to print out the list of list's components. For the target_values list, it would 
# look like: 
# first: 1 second: 2
# first: 3 second: 4
# first: 5 second: 6

dice_value = [1,2,3,4,5,6]

roll_combinations = []

for first_roll in dice_value:
    for second_roll in dice_value:
        roll_combinations.append(
                [first_roll,second_roll]
                )

# Example 3: Every 3 nucleotide combination of RNA
# This example is similar to Example 2, except we are making a list of strings, though it is useful to remember that strings 
# are actually a type of list. As with the above example, print out the strings one at a time.
nucleotides = "ACGU"

nt_list = []

for first in nucleotides:
    for second in nucleotide:
        for third in nucleotide:
            nt_list.append(first + second  + third)


