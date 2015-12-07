import sys
#Need surfaceArea + areaSmallestSide 

total = 0

for line in open('param1.txt'):
	dimen = line.split("x")
	l = int(dimen[0])
	w = int(dimen[1])
	h = int(dimen[2])
	surfaceArea = 2*l*w + 2*w*h + 2*h*l
	extra = min(l*w, w*h, h*l)
	total += (surfaceArea + extra)

print total

'''
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

Your puzzle answer was 1598415.
'''
