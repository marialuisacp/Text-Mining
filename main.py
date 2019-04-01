# -*- coding: utf-8 -*-

from text_mining import TextProcessing
import sys

def main():
	# f=open("teste.txt", "r")
	# if f.mode == 'r':
	# 	contents =f.read()
	# f.close()

	filename = sys.argv[1]
	lines = [line.rstrip('\n') for line in open(filename)]
	
	txtProcessing = TextProcessing()
	txtProcessing.tagging([lines], '.', 'pt')

	# return ''




main()