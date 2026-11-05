# (a) Optimized prime checker function
def is_prime(n):
    if n < 2:
        return False
    d = 2
    # Optimization: only check divisors up to the square root of n (d * d <= n)
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

# (b) Print primes below 50 on one line, then count primes below 100
print("EXPECTED OUTPUT")
print("Primes below 50:", end=" ")
for x in range(2, 50):
    if is_prime(x):
        print(x, end=" ")
print()  # Newline

primes_below_100_count = 0
for x in range(2, 100):
    if is_prime(x):
        primes_below_100_count += 1
print(f"Number of primes below 100: {primes_below_100_count}")

# (c) Goldbach's conjecture solver function
def goldbach(n):
    for p in range(2, n):
        if is_prime(p):
            q = n - p
            if is_prime(q):
                return (p , q) 
            
             # Returns the first pair ( q) where p + q == n
    return None

# Print the pairs for 4, 6, ..., 30
for even_num in range(4, 31, 2):
    pair = goldbach(even_num)
    if pair:
        print(f"The number is :{pair} plus together = {even_num}")

# (d) Verification sweep from 4 to 10,000 using a loop with break
conjecture_holds = True
for even_num in range(4, 10001, 2):
    if not goldbach(even_num):
        conjecture_holds = False
        break  # Stops immediately if a counterexample is discovered

print(f"Goldbach holds for every even number from 4 to 10000: {conjecture_holds}")
