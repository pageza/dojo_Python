#### Find Characters ####
# Write a program thats takes a list of strings, a string with a single character to check for
# Print a new list with all the words containing the character

def findCharacters(list,string):
    newList = []  # Intializes an empty list
    for word in list: # Loops through the list we are given
        if string in word:
            newList.append(word) # If the character is present in the word it appends it to the newList
    return newList







##### Test Cases #####
# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
# new_list = ['hello','world']

test_array = [[word_list,char]]

for test in test_array:
    print findCharacters(test[0],test[1])
