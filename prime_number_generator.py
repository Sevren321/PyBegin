def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(end):
    primes = []
    for num in range(2, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
    
# Example usage
limit = 30
print(f"Prime numbers up to {limit}: {generate_primes(limit)}")