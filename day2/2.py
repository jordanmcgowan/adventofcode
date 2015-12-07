import sys
import heapq
#Need shortestLength + volume 

total = 0

for line in open('param1.txt'):
	demin = line.split("x")
	l = int(demin[0])
	w = int(demin[1])
	h = int(demin[2])
	shortestLength = min((2*l)+(2*w), (2*h)+(2*w), (2*l)+(2*h))
	volume = l*w*h
	total += (shortestLength+volume)

print total

'''
How many total feet of ribbon should they order?

Your puzzle answer was 3812909.
'''