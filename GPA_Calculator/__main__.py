#!/usr/bin/env python3
'''
GPA Calaclator (c) Marc Frankel 2017 | Georgia Tech
'''
import os
import sys
from math import ceil
os.system('')
red = "\u001b[31;1m"
green = "\u001b[32;1m"
yellow = "\u001b[33;1m"
blue = "\u001b[34;1m"
magenta = "\u001b[35;1m"
cyan = "\u001b[36;1m"
reset = "\u001b[0m"

filename = os.path.expanduser("~") + "/GPA_Calculator/data/data.dat"

def main():
	print("GPA Calculator v:0.9.5 (c) Marc Frankel 2017 | Georgia Tech")
	print("Please input your command below: (help for commands)")
	if not os.path.exists(filename):
		os.makedirs(os.path.dirname(filename), exist_ok=True)
		file = open(filename, "w")
		file.close()
	while True:
		command = str(input("$:")).lower()
		if(command in ["quit", "q"]):
			cls()
			quit()
		elif command in ["help", "h"]:
			print("Function Name:        Key")
			print("Quit:                 quit | q")
			print("Help:                 help | h")
			print("Calculate:            calculate | c")
			print("Add:                  add | a")
			print("Delete:               delete | d")
			print("Freshman Forgiveness: forgive | f")
			print("List:                 list | l")
			print("Version:              version | v")
			print("Edit:                 edit | e")
		elif command in ["add", "a"]:
			print(addClass() + " successfully added to record")
		elif command in ["delete", "d"]:
			response = deleteClass()
			if (response[0]) == 1:
				print(response[1] + " was successfully deleted")
			else:
				print(red + "The class: " + response[1] + " was not found"+ reset)
		elif command in ["f","forgive"]:
			response = freshman_forgive()
			if response[0] == 1:
				print(response[1] + " was successfully replaced")
			elif response[0] == 2:
				print(red + "Unable to replace, " + response[1] + " was not taken at Georgia Tech"+ reset)
			else:
				print(red + "The class: " + response[1] + " was not found"+ reset)
		elif command in ["calculate", "c"]:
			typeCalc = str(input("Tech or Hope: "))
			if typeCalc.lower() in ['tech', 't']:
				print("Calculated Tech GPA: " + str(round(techCalculate(),3)))
			elif typeCalc.lower() in ['hope', 'h']:
				print("Calculated Hope GPA: " + str(round(hopeCalculate(),3)))
		elif command in ["version", "v"]:
			print("GPA Calculator v:0.9.5")
		elif command in ["list", "l"]:
			list_class()
		elif command in ["e","edit"]:
			response = edit()
			if response[0] == 1:
				print(response[1])
			else:
				print(red + "The class: " + response[2] + " was not found"+ reset)
		else:
			print(red + "Error: Command '" + command + "' not found. Type 'help' for commands"+ reset)

def hopeCalculate():
	file = open(filename, "r")
	total_hours = 0
	quality_points = 0
	class_list = file.readlines()
	for line in class_list:
		if (line[-1:] == "\n"):
			line = line[:-1]
		class_data = line.split(",")
		if (class_data[2].lower() == "a"):
			points = 4
		elif (class_data[2].lower() == "b"):
			points = 3
		elif (class_data[2].lower() == "c"):
			points = 2
		elif (class_data[2].lower() == "d"):
			points = 1
		else:
			points = 0
		quality_points += (int(class_data[1]) * points)
		total_hours += int(class_data[1])

	gpa = quality_points / total_hours
	return gpa

def techCalculate():
	file = open(filename, "r")
	total_hours = 0
	quality_points = 0
	class_list = file.readlines()
	for line in class_list:
		if (line[-1:] == "\n"):
			line = line[:-1]
		class_data = line.split(",")
		if class_data[3].lower() in ['yes', 'y']:
			if (class_data[2].lower() == "a"):
				points = 4
			elif (class_data[2].lower() == "b"):
				points = 3
			elif (class_data[2].lower() == "c"):
				points = 2
			elif (class_data[2].lower() == "d"):
				points = 1
			else:
				points = 0
			quality_points += (int(class_data[1]) * points)
			total_hours += int(class_data[1])
		else:
			continue

	gpa = quality_points / total_hours
	return gpa

def addClass():
	file = open(filename, "a")
	class_name = str(input("Please enter the class name: "))
	credit_hours = str(input("Please enter the credit hours: "))
	grade = str(input("Please enter your grade: ")).lower()
	tech = str(input("Please indicate if this class was taken at GT (Y/N): ")).lower()
	lines = getClasses()
	for index, line in enumerate(lines):
		if (index + 1) == len(lines):
			if(line[-1:] != "\n"):
				file.write("\n")
	file.write(class_name + "," + credit_hours + "," + grade + "," + tech + "\n")
	file.close()
	return class_name

def deleteClass():
	file = open(filename, "r")
	class_name = str(input("Please enter the class to delete: "))
	lines = file.readlines()
	found = 0
	for line in lines:
		if (class_name == line.split(',')[0]):
			lines.pop(lines.index(line))
			found = 1
	file.close()
	file = open(filename, "w")
	for line in lines:
		file.write(line)
	file.close()
	return [found, class_name]

def getClasses():
	file = open(filename, "r")
	lines = file.readlines()
	file.close()
	return lines

def freshman_forgive():
	file = open(filename, "r")
	class_name = str(input("Please enter the class to replace: "))
	new_grade = str(input("Please enter the new grade: "))
	lines = file.readlines()
	file.close()
	found = 0
	for line in lines:
		if (class_name == line.split(',')[0]):
			mylist = line.split(',')
			mylist[3] = mylist[3].strip()
			location = lines.index(line)
			if mylist[3] in ['y','yes']:
				found = 1
			elif mylist[3] in ['n','no']:
				found = 2
	if found == 1:
		del lines[location]
		old_entry = "*" + mylist[0] + "*," + mylist[1] + "," + mylist[2] + ",n\n"
		new_entry = mylist[0] + "," + mylist[1] + "," + new_grade + ",y\n"
		lines.append(new_entry)
		lines.insert(location,old_entry)
	file = open(filename, 'w')
	for line in lines:
		file.write(line)
	file.close()
	return [found,class_name]

def edit():
	file = open(filename, "r")
	class_name = str(input("Please enter the class to edit: "))
	lines = file.readlines()
	file.close()
	found = 0
	message = class_name + " was successfully updated"
	for line in lines:
		if (class_name == line.split(',')[0]):
			mylist = line.split(',')
			mylist[3] = mylist[3].strip()
			location = lines.index(line)
			found = 1
	if found == 1:
		item_edit = (str(input("1. Name\n2. Credit Hours\n3. Grade\n4. Tech\nWhich item would you like to edit? "))).lower()
		if item_edit in ["1","name"]:
			new_item = str(input("Please enter the new name: "))
			mylist[0] = new_item
			message = class_name + " was successfully replaced with " + new_item
		elif item_edit in ["2", "credit hours"]:
			new_item = str(input("Please enter the new credit hours: "))
			mylist[1] = new_item
		elif item_edit in ["3", "grade"]:
			new_item = str(input("Please enter the new grade: "))
			mylist[2] = new_item	
		elif item_edit in ["4", "tech"]:
			new_item = str(input("Please indicate if this class was taken at GT(Y/N): "))
			mylist[3] = new_item
		if found == 1:
			del lines[location]
			new_entry = mylist[0] + "," + mylist[1] + "," + mylist[2] + "," + mylist[3] + "\n"
			lines.insert(location,new_entry)
		file = open(filename,'w')
		for line in lines:
			file.write(line)
		file.close()
	return [found,message,class_name]

def list_class():
	class_list = getClasses()
	class_name = []
	for line in class_list:
		if (line[-1:] == "\n"):
			line = line[:-1].split(",")
		else:
			line = line.split(",")
		class_name.append(line[0])
	max_len = 0
	for name in class_name:
		if len(name) > max_len:
			max_len = len(name)
	if max_len <= 5:
		top_line = " CLASS | HOURS | GRADE | TECH"
		print(top_line)
		for line in class_list:
			if (line[-1:] == "\n"):
				line = line[:-1].split(",")
			else:
				line = line.split(",")
			rest = "|"+ "   "+ line[1] + "   " + "|"+ "   "+ line[2].upper() + "   "+"|"+ "   "+ line[3].upper() + "   "
			x = len(line[0])
			x = 7-x
			x = ceil(x/2)
			if len(line[0]) %2 != 0:
				entry = " " * x + line[0] + " " * x + rest
			else:
				entry = " " * (x-1) + line[0] + " " * x + rest
			print(entry)
	else:
		x = max_len - 3
		x = ceil(x/2)
		if max_len %2 == 0:
			top_line = " "*(x-1)+"CLASS"+" "*x+"| HOURS | GRADE | TECH"
		else:
			top_line = " "*x+"CLASS"+" "*x+"| HOURS | GRADE | TECH"
		print(top_line)
		for line in class_list:
			if (line[-1:] == "\n"):
				line = line[:-1].split(",")
			else:
				line = line.split(",")
			rest = "|"+ "   "+ line[1] + "   " + "|"+ "   "+ line[2].upper() + "   "+"|"+ "   "+ line[3].upper() + "   "
			if len(line[0]) == max_len:
				entry = " " + line[0] + " " + rest
			else:
				x = len(line[0])
				x = (max_len-x)+2
				x = ceil(x/2)
				if max_len %2 ==0:
					if len(line[0]) %2 != 0:
						entry = " " * (x-1) + line[0] + " " * x + rest
					else:
						entry = " " * x + line[0] + " " * x + rest
				else:
					if len(line[0]) %2 != 0:
						entry = " " * x + line[0] + " " * x + rest
					else:
						entry = " " * (x-1) + line[0] + " " * x + rest
			print(entry)

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

	


if __name__ == "__main__":
	main()