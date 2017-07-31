#### Example Data ####
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

test_array = [sI,mI,bI,eI,spI,sS,mS,bS,eS,aL,mL,lL,eL,spL]


for test in test_array:
    test_variable = test # Choosing a variable to test
    current_type = type(test_variable) # Checking the type of the variable and saving it to a new variable called current_type

    #### Integer ####
    # If the integer is greater than or equal to 100 print "Thats a big number!"
    # If it is less than 100, print "That's a small number"
    if current_type is int:
        if test_variable >= 100:
            print "That's a big number!"
        else:
            print "That's a small number."

    #### String ####
    # if the string is greater than or equal to 50 characters, print "Long Sentence"
    # if shorter than 50 characters, print "Short Sentence"
    elif current_type is str:
        if len(test_variable) >= 50:
            print "Long Sentence"
        else:
            print "Short Sentence"

    #### List ####
    # If the length of the list is greater than or equal to 10, print "Big List!"
    # If length is less than 10, print "Short list."
    elif isinstance(test_variable, list):
        if len(test_variable) >= 10:
            print "Big List!"
        else:
            print "Short List"
