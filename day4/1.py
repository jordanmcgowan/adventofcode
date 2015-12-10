import hashlib

counter = 0
key = 'ckczppom'
answer = str(key)

while answer.startswith('00000') == False:
	counter += 1
	answer = hashlib.md5(str(key + str(counter)).encode()).hexdigest()


print counter

'''
Your puzzle input is ckczppom.

Your puzzle answer was 117946.
'''

#source: https://www.reddit.com/r/adventofcode/comments/3vf4ch/day_4_pseudocode/
#Toughest puzzle to date
