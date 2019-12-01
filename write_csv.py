#!/usr/bin/env python3

def write_csv(file,tuples):
	with open(file, 'w') as fout:
		result='name,address,age'
		for x in tuples:
			result += '\n'
			for z in x[:-1]:
				result += (str(z) + ',')
			result += str(x[-1])
		result += '\n'
		fout.write(result)

tuples_in = [('George','4312 Road', 22),('Joe','54 Love Ave', 21)]
write_csv('/tmp/csv',tuples_in)
