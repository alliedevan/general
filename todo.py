#!/usr/bin/env python
# generates, edits, or removes a .todo file

import os

status = "default"
filename = ""
yes_or_no = ""
jumpout = ""
while status != "exit":

#entrance
	choice = raw_input("\nDo you wish to\n\t1) |Add| a new task?\n\t2) |Edit| an existing task?\n\t3) |Delete| an existing task?\n\t4) |Exit|\n")

	if choice=="1" or choice=="Add" or choice=="add":
		print("So, you wish to add?\n")
		status = "add"
	elif choice=="2" or choice=="Edit" or choice=="edit":
		print("Ah, you wish to edit.  Goodbye!")
		status = "edit"
	elif choice=="3" or choice=="Delete" or choice=="delete":
		print("Yes, it is good to delete.  Goodbye!")
		status = "delete"
	elif choice=="4" or choice=="Exit" or choice=="Exit":
		print("Goodbye!")
		status = "exit"
	else: 
		print("You have chosen an unrecognized option.\nWas it really so hard?")
		status = "exit"


#add
	while status == "add":
		filename = raw_input("What will you call this task?\n(letters only--no file extension please)\n")
		while os.path.exists(r'~/Documents/Todo/' + filename + r'.txt') and jumpout != "yes":
			yes_or_no = raw_input("Task already exists!  Do you wish to edit it?\ny/N\n")
			if yes_or_no == 'y' or yes_or_no == 'Y' or yes_or_no == "yes" or yes_or_no == "Yes":
				status = "edit_from_add"
				jumpout = "yes"
			elif yes_or_no == "" or yes_or_no == "n" or yes_or_no == "N" or yes_or_no == "no" or yes_or_no == "No":
				filename = raw_input("Okay, we need a new name for the task then.\nWhat shall we call it?")
			else:
				print("Invalid input.  Thanks for playing!")
				status = "exit"
				jumpout = "yes"
		jumpout = ""
		os.system(r'touch ~/Documents/Todo/' + filename + r'.txt')	
		print(r'Made ' + filename + r'.txt!  Amazing!')
		status = "ambiguo"

#edit - remember edit_from_add
	if status == "edit" or status == "edit_from_add":
		print("let's edit")



#delete


#exit
	status = "exit"
