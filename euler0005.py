# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def check_divisible(number):
	# Check to see if number generated above is divisible by 11 - 20
	i = 11
	while i < 21:
		if number % i == 0:
			i += 1
		else:
			return False
	return True


number = 2520
while not check_divisible(number):
	number += 2520
	if check_divisible(number):
		print(number)
	else:
		continue