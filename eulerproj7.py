# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


def is_prime(n):
	if n == 1:
		return False
	k = 2
	while k**2 <= n:
		if n % k == 0:
			return False
		k += 1
	return True

cnt = 0
num = 1

while True:
	if is_prime(num):
		cnt += 1
	if cnt == 6: # xth prime number
		break
	num += 1

print(num)