#45.A natural number greater than 1 is called a prime if it has exactly 2 natural factors with the values 1 and this number. 
#Write a program that finds N leading prime numbers. 
#Read the value of N from the keyboard. Using loop statements check that the number N is divisible only by 1 and by N.
#Prime numbers: 2 3 5 7 11 …

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input("Enter the number of prime numbers to find: "))
prime_numbers = []
num = 2

while len(prime_numbers) < N:
    if is_prime(num):
        prime_numbers.append(num)
    num += 1

print(f"The first {N} prime numbers are:", prime_numbers)