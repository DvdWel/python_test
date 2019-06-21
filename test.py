#!/usr/bin/env python3
import random
import re

rules = '''O = Correct position
? = In code but wrong position
X = Not in code'''
opperators = "O?X"

random.seed(a=None, version=2)
solution = ""
for i in range(0,4):
	randNumber = str(random.randrange(0, 10))
	unique = False
	while unique == False:
		counter = 0
		for x in range(0, len(solution)):
			if solution[x] == randNumber:
				randNumber = str(random.randrange(0, 10))
			else:
				counter += 1
			if counter == len(solution):
				unique = True
		if len(solution) == 0:
			unique = True
	solution += randNumber
turn = 0
solved = False
attempt = ""
while solved == False and attempt != "q":
	attempt = input('Enter a 4 digit number:')
	if re.search('(?<!\\d)(?!0000)\\d{4}(?!\\d)', attempt) and attempt != "q":
		if attempt == solution:
			solved = True
		else:
			process = ""
			compared = ""
			for i in range(0, 4):
				match = False
				for x in range(0, 4):
					if attempt[i] == solution[x]:
						if attempt[i] == solution[i]:
							compared += "O"
							match = True
						else:
							compared += "?"
							match = True
				if match == False:
					compared += "X"
			for p in range(0,3):
				for t in range(0,4):
					if compared[t] == opperators[p]:
						process += opperators[p]
			print(process)
			print(rules)
		turn += 1
	else:
		if attempt != "q":
			print("code is not 4 digits")
if solved == True:
	print("cool")
	print("it took you " + str(turn) + " turns")
else:
	print("you gave up after " + str(turn) + " turns")
