# Using only built in methods and functions

#### Find and Replace ####
# In this string: words = "It's thanksgiving day. It's my birthday too!"
# Print the position of the first instance of the word "day"
# Then create a new string where the word "day" is replaced with the word "month"

words = "It's thanksgiving day. It's my birthday too!"

print words.find("day") # Returns 18 for the start of "day"

newString = words.replace("day","month") # Replaces all instances of "day" with "month"

print newString # Returns "It's thanksgiving month. It's my birthmonth too!"


#### Min and Max ####
# Print the min and max values in a list like this one: x = [2,54,-1,7,12,98]

x = [2,54,-1,7,12,98]

print min(x) # Returns -1 for the minimum value
print max(x) # Returns 98 for the maximum value


#### First and Last ####
# Print the first and last values in a list like this one: y = ["hello",2,54,-2,7,12,98,"world"]

y = ["hello",2,54,-2,7,12,98,"world"]

print y[0] # Prints the first indexed position of the y array

print y[len(y)-1] # Calculates the length of the y array,
                  # subtracts 1 since the index starts at 0,
                  # and returns the last position of the y array.

#### New list ####
# Start with a list like this one: z = [19,2,54,-2,7,12,98,10,-3,6]
# Sort it first, then split the list in half.
# Push the list created from the first half to position 0 of the list created
#  from the second half
# Expected output: [[-3,-2,2,6,7],10,12,19,32,54,98]

z = [19,2,54,-2,7,12,98,10,-3,6]

print z # Shows us the starting array
z.sort() # Sorts the array in place from lowest to highest INTEGER values

print z # Shows us our new modified array

first_half = z[:len(z)/2] # Peels off the values starting from 0 "[]" to halve
                          # of the array length "[:len(z)/2]"

second_half = z[len(z)/2:] # Takes the rest of the array from where the last one left off
                           # and the slice ends by default at the end of the list.

print "This is the first halve of the z array",first_half   # Prints the first half of the array
print "This is the second halve of the z array",second_half # Prints the second half of the array

second_half.insert(0,first_half) # Inserts the the array created for the first half at position 0 in the second array.

print second_half # Prints the finished array
