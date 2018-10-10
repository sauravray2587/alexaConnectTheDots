import wikipedia
from connect import giveContent

def findSimilarity(fromNode, toNode):
	''' Decide the order of similarity between two 
		terms on the basis of common words
	'''
	fromNodeContent = giveContent(fromNode).lower()
	toNodeContent   = giveContent(toNode).lower()
	fromNodeWords   = set(fromNodeContent.split(' '))
	toNodeWords     = set(toNodeContent.split(' '))
	commonWords     = len(fromNodeWords.intersection(toNodeWords))
	print(commonWords/min(len(fromNodeWords),len(toNodeWords)))
	# similarityScore  = 
	# print(fromNodeWords)
	# print(toNodeWords)

if __name__ == "__main__":
	startNode = input()
	endNode = input()
	findSimilarity(startNode, endNode)
