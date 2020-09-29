# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

ans = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		prod = str(i*j)
		rev = prod[::-1]
		if prod==rev and int(i*j) > ans:
			ans = int(i*j)
print(ans)