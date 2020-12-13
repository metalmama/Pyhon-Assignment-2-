# This program creates a simple todo list where the user can read and create to do items

# set file name

filename = "todo.txt"

# read in from commandline

import sys
import os

# runs arguments
args = sys.argv

command = args[1]

# switch statement for the below actions
if command not in ("add", "remove", "list"):
    print("Invalid command, Use add/remove/list")

if command == "add":
    print("adding")
elif command == "remove":
    print("removing")
elif command == "list":
    print("listing")
else:
    print("invalid command!")

# read todos
# read in from the file and create an array
# open file
# error handling
try:
    my_file = open(filename, 'r')
    # read from file, tasks is now a list
    tasks = my_file.readlines()
    my_file.close()
except IOError:
    tasks = []
# count the lines
taskcount = len(tasks)
# create todos
if command == "add":
    person = args[2]
    task = args[3]
    # create a numbered new task line
    newtask = person + '|' + task + "\n"
    # add the line to tasks array
    tasks.append(newtask)

elif command == "remove":
    #read from the commandline which is the one you want to delete
    removei = int(args[2])
    #delete list item
    del tasks[removei]

elif command == "list":
    if len(tasks) == 0:
        print("there are no tasks!")
    else:
        #counter
        i=0
        # print("|-----{0}----{1}----|".format("title", "content"))
        #gets rid of the new line character as we do not want it in our array
        striptasks = [task.strip() for task in tasks]
        # the for loop is for each task so each item in tasks becomes one item in the list, this is in the variable task
        for task in striptasks:
            # solid line, is then split into title and content
            title, content = task.split('|')
            # prints it in specified format
            lineformat = "|-{0}----{1}----{2}|"
            print(lineformat.format(i,title, content))
            #adds one to the counter
            i=i+1
else:
    print("invalid command!")

    # save todos

# dump array to same file
my_file = open(filename, 'w')
# write to above file
my_file.writelines(tasks)
my_file.close()
