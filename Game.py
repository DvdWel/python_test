#!/usr/bin/env python3
import random
import re

class Game:

	solution = ""
	turn = 0
	solved = False
	opperators = "O?X"

	def makeSolution(self):
		solutionItem = ""
		for i in range(4):
			randNumber = str(random.randrange(0, 10))
			unique = False
			while unique == False:
				counter = 0
				for x in range(0, len(solutionItem)):
					if solutionItem[x] == randNumber:
						randNumber = str(random.randrange(0, 10))
					else:
						counter += 1
					if counter == len(solutionItem):
						unique = True
				if len(solutionItem) == 0:
					unique = True
			solutionItem += randNumber
		self.solution = solutionItem

	def checkAttempt(self, attempt, solution):
		if re.search('(?<!\\d)(?!0000)\\d{4}(?!\\d)', attempt) and attempt != "q":
			if attempt == solution:
				self.solved = True
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
						if compared[t] == self.opperators[p]:
							process += self.opperators[p]
				print(process)
			self.turn += 1
		else:
			if attempt != "q":
				print("code is not 4 digits")

	def getSolution(self):
		return self.solution