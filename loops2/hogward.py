# students = ["pavan", "bunty", "suraj"]

# for student in range(len(students)) :
#     print(student + 1, students[student])

# dictionary
# students = {
#     "Pavan" : "Red", 
#     "Sheryas" : "Yellow", 
#     "Surya" : "Green", 
# }

# for student in students:
#     print(student ,students[student], sep=", ")

students = [
    {"name": "Pavan", "House": "Red", "Position": "Co-leader"},
    {"name": "Sheryas", "House": "Yellow", "Position": "Bandset"},
    {"name": "Surya", "House": "Green", "Position": "Member"},

]

for student in students :
    print(student["name"], student["House"], student["Position"], sep=", ")