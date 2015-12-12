import sys


'''
def repeatChars(s):
	for c1, c2 in s:
		print ""
'''

count = 0

for line in open('input.txt'):
	if count == 0:
		i = 0
		zipped = zip(line, line[1:])
		for a in zipped[i]:
			print zipped[i]
			print a
		i += 1
	