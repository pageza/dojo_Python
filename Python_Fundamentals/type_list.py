#### Type List ####
# Write a program that takes a list and prints a message for each element in the list, based on that lists data type.
# Input will always be a list, for item in the list, test the data type.
# If the item is a string, concatenate it onto a new string.
# If it is a number, add it to the running sum.
# At the end, print the string, the sum and an analysis of what the list containts


def list_item_type(test):
    newString = "" # Creates a new empty string
    sum = 0 # Intializes the sum to 0

    for item in test:  # Loops through the list
        if isinstance(item,int) or isinstance(item,float):
            sum += item # If the type is a number(integers or floats) it adds the number to the sum
        elif isinstance(item,str):
            newString += item # If the type is a string it adds teh string the the newString varibale

    if newString and sum:   # If a newString and a sum both have values then it diverts into this branch
        print "This is a mixed array"
        print "The sum is : ", sum
        print "The string is : ", newString

    elif newString: # If only the presence of values are in newString it goes down this branch
        print "This is an array of strings"
        print "The string : ", newString

    else: # Assumes all other cases hace been caught and addresses the last possible outcome.
        print "This is an array of integers"
        print "This is the sum : ", sum


###### Test Cases #########
#input 1
l = ['magical unicorns',19,'hello',98.98,'world']
#output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"

# input 2
m = [2,3,1,7,4,12]
#output
# "The list you entered is of integer type"
# "Sum: 29"

# input 3
n = ['magical','unicorns']
#output
# "The list you entered is of string type"
# "String: magical unicorns"

test_array = [l,m,n]

for value in test_array:
    print list_item_type(value)
