# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

lcm = 1
x = 1 #from~
y = 20 #~to ' s Least Common Divisor

for i in range(x, y+1):
	a = 1
	while 1 <= a <= i:
		if lcm % i == 0:
			break
		else:
			lcm = int(lcm / a)
			a += 1
			lcm = lcm * a


print(lcm)
