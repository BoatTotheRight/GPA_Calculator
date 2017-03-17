#!/usr/bin/env python3
'''
GPA Calaclator (c) Marc Frankel 2017 | Georgia Tech
'''
import os
import sys
filename = os.path.expanduser("~") + "/GPA_Calculator/data/data.dat"

def main():
	print("GPA Calculator v:0.9.5 (c) Marc Frankel 2017 | Georgia Tech")
	print("Please input your command bellow: (help for commands)")
	if not os.path.exists(filename):
		os.makedirs(os.path.dirname(filename), exist_ok=True)
		file = open(filename, "w")
		file.close()
	while True:
		command = str(input("$:")).lower()
		if(command in ["quit", "q"]):
			quit()
		elif command in ["help", "h"]:
			print("Function Name: Key")
			print("Quit:      quit | q")
			print("Help:      help | h")
			print("Calculate: calculate | c")
			print("Add:       add | a")
			print("Delete:    delete | d")
			print("List:      list | l")
			print("Version:	  v | version")
		elif command in ["add", "a"]:
			print(addClass() + " successfully added to record")
		elif command in ["delete", "d"]:
			response = deleteClass()
			if (response[0]) == 1:
				print(response[1] + " was successfully deleted")
			else:
				print("The class: " + response[1] + " was not found")
		elif command in ["calculate", "c"]:
			print("Calculated GPA: " + str(round(calculate(), 3)))
		elif command in ["version", "v"]:
			print("GPA Calculator v:0.9.5")
		elif command in ["list", "l"]:
			class_list = getClasses()
			print("CLASS | HOURS | GRADE")
			for line in class_list:
				if (line[-1:] == "\n"):
					line = line[:-1].split(",")
				else:
					line = line.split(",")
				print(line[0] + " | " + line[1] + " | " + line[2].upper())
		else:
			print("Error: Command '" + command + "' not found. Type 'help' for commands")

def calculate():
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
			points = 0;
		quality_points += (int(class_data[1]) * points)
		total_hours += int(class_data[1])

	gpa = quality_points / total_hours
	return gpa
		
def addClass():
	file = open(filename, "a")
	class_name = str(input("Please enter the class name: "))
	credit_hours = str(input("Please enter the credit hours: "))
	grade = str(input("Please enter your grade: ")).lower()
	lines = getClasses()
	for index, line in enumerate(lines):
		if (index + 1) == len(lines):
			if(line[-1:] != "\n"):
				file.write("\n")
	file.write(class_name + "," + credit_hours + "," + grade + "\n")
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

if __name__ == "__main__":
	main()