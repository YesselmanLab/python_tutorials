# Bug busters. 
# The issue here is that the number is not passed to the function. This can be fixed in the following:
def absolute_value(number):
    if number < 0:
        number *= -1
    return number

def squared(input_number):
    return input_number*input_number

def min_value_list(input_list):
    minimum = input_list[0]
    for num in input_list:
        if num < minimum:
            minimum = num
    return minimum

def is_valid_structure(input_ss):
    left_paren = input_ss.count('(')
    right_paren = input_ss.count(')')
    dots = input_ss.count('.')

    if left_paren != right_paren:
        return False
    elif len(input_ss) != (left_paren + right_paren + dots):
        return False
    else:
        return True