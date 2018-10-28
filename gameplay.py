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
		return self.hintsLeft

	def useHints(self):
		if self.hintsLeft>0:
			self.hintsLeft -=1
			return True
		else:
			return False

	def updateScore(self, score, moves):
		if score==1:
			self.score = self.score+score-(0.1*(moves-5))


class Game:
	def __init__(self, name1, name2):
		self.Team1 = Team(name1)
		self.Team2 = Team(name2)
		self.curTeam = self.Team1
		self.status = 0
		self.roundNumber = 0

	def __str__(self):
		return "An instance of class Game with state: Team1=%s Team2=%s and status=%s" % (self.team1, self.team2, self.status)

	def updateGameStatus(self):
		if self.Team1.score > self.Team2.score:
			self.status = 1
		else:
			self.status = 2

	def curRound(self):
		''' The game will be started from startNode and 
		will end until we reach endNode
		'''
		print("%s, give us the two endpoints" %(self.curTeam.name))
		startNode = input()
		endNode   = input()
		moves = 0
		score = 0
		prevNode = startNode
		while prevNode!=endNode:
			text = input()
			if text is "check":
				print(prevNode,endNode)
			else:
				curNode = text
				moves += 1 

			if checkConnection(prevNode, curNode) is True:
				prevNode = curNode
			elif checkConnection(curNode, prevNode) is True:
				prevNode = curNode
			elif findSimilarity(prevNode,curNode) is True:
				prevNode = curNode

			else:
				print("Not a Valid Connection, Try Again.")
			if moves>=15:
				self.curTeam.updateScore(score, moves)		
				return

		score = 1;
		self.curTeam.updateScore(score, moves)

	def getGameStatus(self,Team1,Team2):
		if self.status==1:
			return "%s is winning with a score of %s and %s has a score of %s "%(Team1.name,Team1.score,Team2.name,Team2.name)
		if self.status==2:
			return "%s is winning with a score of %s and %s has a score of %s "%(Team2.name,Team2.score,Team1.name,Team1.name)
		if self.status ==0:
			return "Both the teams are at the same score of %s"%(Team1.score)


	def gameModerator(self):
		rounds  = 5
		for i in range(0,2*rounds):
			self.roundNumber += 1
			if i%2==0:
				self.curTeam = self.Team1
				self.curRound()
			else:
				self.curTeam = self.Team2
				self.curRound()


def createGame():
	print("Give the names of the two teams")
	name1 = input()
	name2 = input()
	Game1 = Game(name1, name2)
	Game1.gameModerator()


if __name__ == "__main__":
	createGame()
