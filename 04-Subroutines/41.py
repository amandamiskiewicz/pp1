'''41.	Define the function f(n) that returns the n-th prime number.
A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:
f(1) returns 2
f(5) returns 11
'''

def f(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    
    return primes[-1]




if __name__=="__main__":
    print(f(1))
    print(f(5))