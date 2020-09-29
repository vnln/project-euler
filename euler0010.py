# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


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

sum = 0
for i in range(2000000):
    if prime_check(i):
        sum += i
print(sum)

