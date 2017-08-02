#### Stars ####
# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.

def draw_stars(thing):
    for x in thing:
        print "*" * x

draw_stars([1,2,3,4,5,6])

def draw_characters(list):
    for x in list:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            character = x[0].lower()
            print character * length

test_list = [6,"Zach",3,"Texas","Dallas",15]

draw_characters(test_list)
