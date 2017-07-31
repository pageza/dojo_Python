#### Compare Arrays #####
# Write a program that compares to lists and prints a message
# depending on if they are indentical or not.

def isIdentical(list_one,list_two):
    if len(list_one) != len(list_two):  # This checks for a base case where the lists have inequal length and therefore cannot be indentical
        return "The lists are NOT indentical"

    for item in range(len(list_one)): # This creates a loop where I can check the same indexes for different lists and the values for indentical
        if list_one[item] != list_two[item]: # if the values do not match this catches it and returns the appropriate response
            return "The lists are NOT indentical"
    return "The lists ARE indentical" # The loop completed without finding any different values.

#### Test Data #####
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_a = [1,2,5,6,5]
list_b = [1,2,5,6,5,3]

list_three = [1,2,5,6,5,16]
list_four = [1,2,5,6,5]

list_c = ['celery','carrots','bread','milk']
list_d = ['celery','carrots','bread','cream']

test_array = [[list_one,list_two],[list_a,list_b],[list_three,list_four],[list_c,list_d]]

for test in test_array:
    print isIdentical(test[0],test[1])
