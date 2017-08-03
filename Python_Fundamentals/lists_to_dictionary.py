# Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. Assume the lists will be of equal length.
#
# Your first function will take in two lists containing some strings. Here are two example lists:
#
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dictionary(list1,list2):
    newDictionary = {}
    for i in range(0,len(list1)):
        newDictionary[list1[i]]=list2[i]
    return newDictionary

print make_dictionary(name,favorite_animal)
