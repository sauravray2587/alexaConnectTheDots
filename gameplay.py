class team:
	def __init__(self, name):
        self.name  = name
        self.score = 0
        self.moves = 0

    def change_name(self, new_name):
        self.name = new_name

    def giveScore(self):
    	return self.score

    def giveMoves(self):
    	return self.moves


class Game:
	def __init__(self, name1, name2):
		self.team1 = name1
		self.team2 = name2
		# 0 - Tie 1 - Team1 2 - Team2
		self.status = 0

def createGame:
	name1 = input()
	name2 = input()
	Game = Game(name1, name2)
	return Game
