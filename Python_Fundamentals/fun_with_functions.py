##### Fun with Functions ######

#### Odd/Even ####
# Create a function called odd_even that counts from 1 to 2000
# As the loop executes print the number of the iteration as well as if its even or odd

def odd_even():
    for i in range(1,2000):
        if (i % 2 == 0):
            print "The number ", i ," is even"
        else:
            print "The number ", i ," is odd"

odd_even()

#### Multiply ####
# Create a function called multiply that iteates through each value in a list
# and returns a list where each value has been multiplied by 5

def multiply(list):
    newList = []
    for i in list:
        newList.append(i*5)
    return newList

print multiply([1,2,3,4])

#### hacker challenge ####
# Write a function that takes the multiply function as an arg
# should return the multiplied list as a two-dimensioal list
# Each internal list should contains the original number
