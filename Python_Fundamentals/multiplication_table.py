##### Multiplication Table ######
# Print a mulitplaction table

def multiplication_table():
    print " x 1 2 3 4 5 6 7 8 9 10 11 12" # this prints the top row of numbers to multipy along the x axis
    for row in range(1,12+1): # This compiles the rows one at a time
        display = "" # Intializes an empty string to build the row inside of
        for column in range(0,12+1): # this compiles the columns one row at a time
            if column is 0:
                display += ' '+ str(row) # if it is the first column we won't do any math, just show the number to be multiplied along the y axis
            else:
                display += ' '+ str(column * row) # if its not the first column we start doing our math and adding it to the row's display
        print display # Prints the newly created row and goes back up the loop to start on the next iteration

multiplication_table()
