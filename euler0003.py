"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

num=600851475143
res=2
while num>1:
	while num%res:
		res+=1
	num=num/res
print(res)