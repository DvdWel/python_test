#!/usr/bin/env python3
import random
from Player import Player
from Game import Game

rules = '''O = Correct position
? = In code but wrong position
X = Not in code'''

game = Game()
player = Player()

random.seed(a=None, version=2)
solution = ""
print(rules)
game.makeSolution()
solution = game.getSolution()
print(solution)
turn = 0
solved = False
attempt = ""
while game.solved == False and attempt != "q":
	player.makeGuess()
	attempt = player.getGuess()
	game.checkAttempt(attempt, solution)
if game.solved == True:
	print("cool")
	print("it took you " + str(game.turn) + " turns")
else:
	print("you gave up after " + str(game.turn) + " turns")
