##### Checkerboard ######
# Write a program that prints a checkerboard pattern of '*'
# Should take no input

def checkerboard():
    for i in range(1,10):
        if (i%2==0):
            print "* * * * * * * * * * * "
        else:
            print " * * * * * * * * * * *"

checkerboard()
