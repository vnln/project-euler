# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

nums = 100
sum = nums*(nums+1)/2
sum_sq = (2*nums+1)*(nums+1)*nums//6
print(int(sum**2 - sum_sq))