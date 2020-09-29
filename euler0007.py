# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def prime_check(n):
    if n <= 1:
        return False
    elif n < 4:
        return True
    elif not (n % 2 and n % 3):
        return False
    elif n < 9:
        return True
    else:
        f = 5
        while f <= n**0.5:
            if not(n % f and n % (f+2)):
                return False
                break
            f += 6
    return True
    

count = 1
current = 1
while count != 10001:
    current += 2
    if prime_check(current):
        count += 1
    
print(current)
