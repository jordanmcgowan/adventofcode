import hashlib

counter = 0
key = 'ckczppom'
answer = str(key)

while answer.startswith('000000') == False:
	counter += 1
	answer = hashlib.md5(str(key + str(counter)).encode()).hexdigest()


print counter

'''
Your puzzle input is ckczppom.

Your puzzle answer was 3938038.
'''