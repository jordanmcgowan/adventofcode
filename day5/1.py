'''
A nice string is one with all of the following properties:

    It contains at least three vowels
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
'''

import sys

def consecCheck(s):
	return any(c1 == c2 for c1, c2 in zip(s, s[1:]))

def findVowels(s):
	vowels = ['a', 'e', 'i', 'o', 'u']
	vowelCount = 0

	for char in s:
		if char in vowels:
			vowelCount += 1 

	if vowelCount >= 3:
		return True

	elif vowelCount < 3:
		return False

count = 0

for line in open('input.txt'):
	print line

	#Check to see if there are 3 vowels
	if not findVowels(line):
		print 'fail vowels'
		count += 1

	#Check for special chars
	elif 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
		print 'fail special char'
		count += 1

	elif not consecCheck(line):
		print 'fail consecutive'
		count += 1 


print 1000 - count

'''
How many strings are nice?

Your puzzle answer was 255.
'''