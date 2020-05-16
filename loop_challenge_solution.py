
table_size = input("enter size of table")

elments = range(1,1+table_size)


output_str = ""

for multiplier in elments:
    for elem in elments:
        output_str+= str(elem*multiplier) + " "
    output_str += "\n"

print(output_str)

# 1 2 3
# 2 4 6 
# 3 6 9

# [1,2,3]

# outer inner
# 1     1
# 1     2
# 1     3
# 2     1
# 2     2
# 2     3
# 3     1
# 3     2
# 3     3 
