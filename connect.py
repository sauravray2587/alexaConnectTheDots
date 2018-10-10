import requests
from bs4 import BeautifulSoup
import wikipedia
'''
	1) Find Valid connections
	2) All connections on wikipedia are not relevant
	3) Find valid sentences
'''
def giveSentences(content):
	sentences = content.split('.')
	return sentences

def giveContent(searchTerm):
	print("Wait for the Result")
	searchTerm = wikipedia.search(searchTerm)[0]
	page = wikipedia.page(searchTerm)
	content = page.content
	return content

def checkConnection(fromNode, toNode):
	'''To check whether term1 is directly related to 
		term2 and if it is directly related to, state
		the connection.
	'''
	sentences = giveSentences(fromNode)
	# print(sentences[0])
	y = []
	for x in sentences:
		if toNode in x:
			y.append(x)
	# print(y[0])
	if len(y) is 0:
		return False
	else:
		print(y[0])
		return True


def startGame(startNode, endNode):
	''' The game will be started from startNode and 
	will end until we reach endNode
	'''
	prevNode = startNode
	while prevNode!=endNode:
		text = input()
		if text is "check":
			print(prevNode,endNode)
		else:
			curNode = text

		if (checkConnection(prevNode, curNode) or findSimilarity(prevNode,curNode)) is True:
			prevNode = curNode
		else:
			print("Not a Valid Connection, Try Again.")


def takeInputs():
	startNode = input()
	endNode = input()
	startGame(startNode, endNode)
