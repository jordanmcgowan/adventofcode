'''
A nice string is one with all of the following properties:

    It contains at least three vowels
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
'''

import sys
import re

def consecCheck(s):
	return bool(re.search(r'(.)\1', s))

def findVowels(s):
	vowels = ['a', 'e', 'i', 'o', 'u']
	count = 0

	for char in s:
		if char in vowels:
			print char
			count += 1 

	if char >= 3:
		return True

count = 0

for line in open('input.txt'):

	if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
		print 'fail'
		count += 1

	elif consecCheck(line):
		print 'fail'
		count += 1 

	elif findVowels(line):
		print 'fail'
		count += 1

print count

#515 too high