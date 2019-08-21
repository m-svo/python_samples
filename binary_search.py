#!/usr/bin/env python3

def search(seq,item):
	for index in range(len(seq)):
		if seq[index] == item:
			return index
	if item not in seq:
		return -1

print (search(([1,4,5,8,10,16]),10))
print (search(([1,4,5,8,10,16]),18))
print (search(([1,4,5,8,10,16]),4))
