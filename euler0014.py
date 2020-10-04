# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?


def collatz(i):
    if i in leng:
        return leng[i]
    elif i % 2 == 0:
        leng[i] = 1 + collatz(i // 2)
    else:
        leng[i] = 2 + collatz(i * 3 + 1)
    return leng[i]


leng = {1: 1}
max_num, max_len = 0, 0
for x in range(500000, 1000000):
    if collatz(x) > max_len:
        max_len = collatz(x)
        max_num = x
print(max_num)
