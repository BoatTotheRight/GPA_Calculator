#!/usr/bin/env python3
'''
GPA Calaclator (c) Marc Frankel 2017 | Georgia Tech
'''
import os
import sys
filename = os.path.expanduser("~") + "/GPA_Calculator/data/data.dat"

def main():
	print("GPA Calaclator (c) Marc Frankel 2017 | Georgia Tech")
	print("Please input your command bellow: (help for commands)")
	if not os.path.exists(filename):
		os.makedirs(os.path.dirname(filename), exist_ok=True)
		file = open(filename, "w")
		file.close()
	while True:
		command = input("$:")
		if(str(command).lower() in ["quit", "q"]):
			quit()
		elif str(command).lower() in ["help", "h"]:
			print("Function Name: Key")
			print("Quit:      quit | q")
			print("Help:      help | h")
			print("Calculate: calculate | c")
			print("Add:       add | a")
			print("Delete:    delete | d")
			print("List:      list | l")
		elif str(command).lower() in ["add", "a"]:
			print(addClass() + " successfully added to record")
		elif str(command).lower() in ["delete", "d"]:
			response = deleteClass()
			if (response[0]) == 1:
				print(response[1] + " was successfully deleted")
			else:
				print("The class: " +response[1] + " was not found")
		elif str(command).lower() in ["calculate", "c"]:
			print("Calculated GPA: " + str(round(calculate(), 3)))
		elif str(command).lower() in ["list", "l"]:
			class_list = getClasses()
			print("CLASS | HOURS | GRADE")
			for line in class_list:
				line = line[:-1].split(",")
				print(line[0] + " | " + line[1] + " | " + line[2].upper())
		else:
			print("Error: Command '" + command + "' not found. Type 'help' for commands")

def calculate():
	file = open(filename, "r")
	total_hours = 0
	quality_points = 0
	class_list = file.readlines()
	for line in class_list:
		line = line[:-1]
		class_data = line.split(",")
		if (class_data[2] == "a"):
			points = 4
		elif (class_data[2] == "b"):
			points = 3
		elif (class_data[2] == "c"):
			points = 2
		else:
			points = 1
		quality_points += (int(class_data[1]) * points)
		total_hours += int(class_data[1])

	gpa = quality_points / total_hours
	return gpa
		
def addClass():
	file = open(filename, "a")
	class_name = str(input("Please enter the class name: "))
	credit_hours = str(input("Please enter the credit hours: "))
	grade = str(input("Please enter your grade: ")).lower()
	file.write(class_name + "," + credit_hours + "," + grade + "\n")
	file.close()
	return class_name

def deleteClass():
	file = open(filename, "r")
	class_name = str(input("Please enter the class to delete: "))
	lines = file.readlines()
	found = 0
	for line in lines:
		if (class_name in line):
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
	return file.readlines()

#Main Init loop
if __name__ == "__main__":
	main()
