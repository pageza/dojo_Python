##### Names #####
# Part I
# Given the following list:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# Create a program that outputs:
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

for student in students:
    print student["first_name"] +' '+ student["last_name"]

# Part II
# Now, given the following dictionary:
#
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
# Create a program that prints the following format (including number of characters in each combined name):
# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

print "Students"
for student in users["Students"]:
    length = len(student["first_name"])+len(student["last_name"])
    print student["first_name"].upper() + " " + student["last_name"].upper() + "-", length
for instructor in users["Instructors"]:
    length = len(instructor["first_name"])+len(instructor["last_name"])
    print instructor["first_name"].upper() + " " + instructor["last_name"].upper() + "-", length
