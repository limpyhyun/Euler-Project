# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers


ans = 0

for a in range(1000, 10000):
	for b in range(1000, 10000):
		if a*b > ans:
			if str(a*b) == (str(a*b))[::-1]:
				ans = a * b

print(ans)