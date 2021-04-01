# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers


mylist = []

for a in range(100, 1000):
	for b in range(100, 1000):
		n = str(a*b)
		if 10000 <= a*b < 100000:
			if n[:2] == (n[3:])[::-1]:
				mylist.append(a*b)
		elif 100000 <= a*b < 1000000:
			if n[:3] == ((n[3:])[::-1]):
				mylist.append(a*b)

mylist = set(mylist)
mylist = list(mylist)
mylist.sort()

print(mylist[-1])