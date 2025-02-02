# -*- coding: utf-8 -*-

from text_mining import TextProcessing
import sys
import nltk
from nltk.corpus import floresta

def main():
	# def simplify_tag(t):
	#     if "+" in t:
	#         return t[t.index("+")+1:]
	#     else:
	#         return t
	
	# tsents = floresta.tagged_sents()
	# tsents = [[(w.lower(),simplify_tag(t)) for (w,t) in sent] for sent in tsents if sent]
	# train = tsents[100:]
	# print train

	lines = []

	filename = sys.argv[1]
	for line in open(filename):
		lines.append(line)
		# sentence = []
		# words = line.split()
		# for word in words:
		# 	sentence.append(word);
		# lines.append(sentence);

	txtProcessing = TextProcessing()
	dataDocuments = txtProcessing.tokenize(lines)
	txtProcessing.tagging(dataDocuments, '.', 'pt')

main()
