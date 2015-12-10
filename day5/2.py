import sys


'''
def repeatChars(s):
	for c1, c2 in s:
		print ""
'''


for line in open('input.txt'):
	print zip(line, line[1:])
