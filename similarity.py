import graphlab

import wikipedia
from connect import giveContent
import math
import numpy as np
import sklearn
from nltk.corpus import stopwords

def findSimilarity(fromNode, toNode):
	''' Decide the order of similarity between two
		terms on the basis of common words
	'''
	fromNodeContent = (giveContent(fromNode).lower()).split()
	toNodeContent   = (giveContent(toNode).lower()).split()
	stop_words = set(stopwords.words('english'))
	fromDict = {}
	for word in fromNodeContent:
		if word not in stop_words:
			if word in fromDict:
				fromDict[word] += 1
			else:
				fromDict[word] = 1
	toDict = {}
	for word in toNodeContent:
		if word not in stop_words:
			if word in toDict:
				toDict[word] += 1
			else:
				toDict[word] = 1

	fromNodeWords   = set(fromDict)
	toNodeWords     = set(toDict)
	commonWords     = fromNodeWords.intersection(toNodeWords)

	dotProduct = 0
	for word in commonWords:
		dotProduct += fromDict[word]*toDict[word]
	magFrom = 0
	for word in fromDict:
		magFrom += fromDict[word]*fromDict[word]
	magTo = 0
	for word in toDict:
		magTo += toDict[word]*toDict[word]
	print(dotProduct/math.sqrt(magTo*magFrom),"DOT PRODUCT USED")
	return dotProduct/math.sqrt(magTo*magFrom)
# print(commonWords/min(len(fromNodeWords),len(toNodeWords)))
	# similarityScore  = 
	# print(fromNodeWords)
	# print(toNodeWords)


def findSimilarityBetweenPeople(firstPerson, secondPerson):
	try:
		personA = people[people['name'] == firstPerson]
		personB = people[people['name'] == secondPerson]
		return graphlab.distances.cosine(personA['tfidf'][0], personB['tfidf'][0])
	except Exception as _:
		return -1


if __name__ == "__main__":
	startNode = input()
	endNode = input()
	graphlab.product_key.set_product_key("E5E5-ED7D-D84A-5C81-3D1D-9778-1370-F123")
	graphlab.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', 4)
	people = graphlab.SFrame('people_wiki.gl/')
	people['word_count'] = graphlab.text_analytics.count_words(people['text'])
	tfidf = graphlab.text_analytics.tf_idf(people['word_count'])

	# Earlier versions of GraphLab Create returned an SFrame rather than a single SArray
	# This notebook was created using Graphlab Create version 1.7.1
	if graphlab.version <= '1.6.1':
		tfidf = tfidf['docs']
	people['tfidf'] = tfidf
	similarity=findSimilarityBetweenPeople(startNode,endNode)
	boolean_closeness=0
	if similarity > 0.9:
		boolean_closeness=1
	if similarity !=-1:
		similarity=findSimilarity(startNode, endNode)
		if similarity>0.3:
			boolean_closeness=1


