#!/usr/bin/env python3
import random

class Game:

	solution = ""

	def makeSolution(self):
		solution = ""
		for i in range(4):
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
		self.solution = solution

	def getSolution(self):
		return self.solution