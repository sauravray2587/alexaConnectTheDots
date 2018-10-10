from connect import *
from similarity import *

class Team:
	def __init__(self, name):
		self.name  = name
		self.score = 0
		self.moves = 0
		self.hintsLeft = 2

	def change_name(self, new_name):
		self.name = new_name

	def giveScore(self):
		return self.score

	def giveMoves(self):
		return self.moves

	def checkHints(self):
		if self.hintsLeft > 0:
			return True
		else:
			return False
	def updateScore(self):




class Game:
	def __init__(self, name1, name2):
		self.team1 = name1
		self.team2 = name2
		Team1 = new Team(name1)
		Team2 = new Team(name2)
		# 0 - Tie 1 - Team1 2 - Team2
		self.status = 0

	def __str__(self):
		return "An instance of class Game with state: Team1=%s Team2=%s and status=%s" % (self.team1, self.team2, self.status)

	def updateGameStatus(self, Team1, Team2):
		if Team1.score > Team2.score:
			self.status = 1
		else:
			self.status = 2


def createGame():
	name1 = input()
	name2 = input()
	Game1 = Game(name1, name2)
	print(Game1)
	



if __name__ == "__main__":
	createGame()