#  Scores and Grades
# Write a function that generates ten scores between 60 and 100.
# Each time a score is generated, your function should display what the grade is
# Here is the grade table:
#
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

def letter_grades(score):
    if score <= 69:
        return "Your score of : "+ str(score)+ "  recieves a letter grade of : D"
    elif (69<score<=79):
        return "Your score of : "+ str(score)+ "  recieves a letter grade of : C"
    elif (79<score<=89):
        return "Your score of : "+ str(score)+ "  recieves a letter grade of : B"
    elif (89<score):
        return "Your score of : "+ str(score)+ " recieves a letter grade of : A"

grades = [100,89,85,79,75,69,65,50]

for grade in grades:
    print letter_grades(grade)
