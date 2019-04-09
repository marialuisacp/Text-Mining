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

	# print lines
	# # lines = [line.rstrip(' ') for line in open(filename)]
	
	txtProcessing = TextProcessing()
	# txtProcessing.tagging(lines, '.', 'pt')

	dataDocuments = txtProcessing.tokenize(lines)
	# without_accent = txtProcessing.remove_accents(dataDocuments)
	# nao_desistir = txtProcessing.tokenizeBigram(teste)
	# print nao_desistir

	txtProcessing.tagging(dataDocuments, '.', 'pt')

main()
