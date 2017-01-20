# Python Parsing for Piskel (www.piskelapp.com)
#
# Giovanni Gentile
# January 2017
#
# Instructions:
# Download your design by "Export" in C file,
# and open the Python file with python piskel_parsing.py in Temrinal

import re
lst=[]

print '---------------------\nParsing PISKEL v1.0\nGiovanni Gentile 2017'
fname = raw_input("Enter file name: ")
fh = open(fname)

print '---------------------\n\nNeopixel Sprite\n'
for line in fh:
	line = line.rstrip()
	#print line
	line = line.split()
	for word in line:
		word = word.split()
		#print word
		#word = str(word)


		if word == ['0x00000000,'] or word == ['0x00000000']:
			#print '0'
			lst.append('0')

		elif word == ['0xff000000,'] or word == ['0xff000000']:
			#print '1'
			lst.append('1')

lst.insert(0,'B')
lst.insert(9,',''\n''B')
lst.insert(18,',''\n''B')
lst.insert(27,',''\n''B')
lst.insert(36,',''\n''B')
lst.insert(45,',''\n''B')
lst.insert(54,',''\n''B')
lst.insert(63,',''\n''B')
print ''.join(lst)

print '---------FINE--------\n'
