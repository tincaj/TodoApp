print "Welcome to my TODO App"

"""
name = "Tina"
surname = "Juric"

names = ["Tina", "Spela", "Bella"]

user =[name, surname]

print names [0]
"""

todo_list = []

todo_dictionary = {}

while True:
    task = raw_input("Please enter a TODO task: ")
    todo_list.append(task)

    complete = raw_input("Is task finished (yes/no): ")

    if complete.lower() == "yes":
        todo_dictionary [task] = True
    else:
        todo_dictionary [task] = False

    print "Your task is " + task

    newTask = raw_input("Would you like to add another task? ")

    if newTask == "no":
        break

todo_file = open ("todo.txt", "w+")

print "Zakljuceni taski: "
todo_file.write ("Zakljuceni taski: \n")

for task in todo_dictionary:
    if todo_dictionary [task]: #if todo_dictionary [task] == True:
        print task
        todo_file.write ("- " + task + "\n")

print "Nezakljuceni taski: "

for task in todo_dictionary:
    if not todo_dictionary [task]: #if todo_dictionary [task] == False:
        print task
        todo_file.write ("- " + task + "\n")

"""
for task in todo_list:
    print task
"""

print "END"
