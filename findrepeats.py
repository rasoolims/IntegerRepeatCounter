#! /usr/bin/python
# coding=utf8

'''
	This is a simple program to find repeated integers
'''

__author__="Mohammad Sadegh Rasooli <rasooli@cs.columbia.edu>"
__date__ ="Feb, 2013"

import sys
import operator

'''
	finds and prints repeated integers
'''
def findintegers(array):
	freqDict=dict()
	for value in array:
		if freqDict.has_key(value):
			freqDict[value]+=1
		else:
			freqDict[value]=1
	freqDict=sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
	for f in freqDict:
		print f[0],'occured '+str(f[1])+' time(s)'


'''
	Main body
'''

if len(sys.argv)>1 and sys.argv[1]=='--help':
	print 'This is a simple program to find repeated integers'
	print 'python findrepeats.py < [inputfile]'
	sys.exit(0)

arr=list()
while True:
	try:
		line=raw_input('')
		if line:
			try: 
				arr.append(int(line))
			except:
				sys.stderr.write('Error! Everything in the input should be integer.\n')
				sys.stderr.write('Problem with the input '+line.strip()+'\n')
				sys.exit(0)
	except EOFError:
		break
findintegers(arr)