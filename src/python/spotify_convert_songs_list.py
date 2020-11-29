import os
import sys
import numpy as pn

#--------------------------------------------------------------------------------
def loadList(filename):

	#Read
	textdata = []
	with open(filename,'r') as f:
		for line in f:
			textdata.append(line)

	#Return
	return textdata

#--------------------------------------------------------------------------------
if __name__ == '__main__':

	#Load load
	textdata = loadList('../../data/delicieuse_musique/complete/songs3.txt')

	#Remove spaces
	textdata = textdata[0].replace(' ','')

	#Split
	textdata = textdata.split('),(')
	textdata[0] = textdata[0][2:]
	textdata[-1] = textdata[-1][:-2]

	#Store
	with open('../../data/delicieuse_musique/complete/songs_cleaned3.txt','w') as f:
		for item in textdata:
			elements = item.split(',')
			f.write(elements[0].replace("'",'') + '\n')

