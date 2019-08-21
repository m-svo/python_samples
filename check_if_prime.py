#!/usr/bin/env python3

def is_prime(n):
	sq_root = (n**.5)
	sq_root_int = int(round(sq_root))
	test_numbers = range(2,n)
	non_prime = False
	for x in test_numbers:
		if n % x == 0:
			non_prime = True
			break
	if non_prime:
		return False
	else:
		return True

print (is_prime(587))
