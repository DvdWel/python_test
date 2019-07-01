#!/usr/bin/env python3
import random
import re

class Player:

	guess = ""

	def makeGuess(self):
		attempt = input('Enter a 4 digit number:')
		self.guess = attempt

	def getGuess(self):
		return self.guess