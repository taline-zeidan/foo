# Write your code below this line 👇
import math
def prime_checker(number):
    if number <= 1:
        is_prime = False
    elif number <= 3:
        is_prime = True
    elif number % 2 == 0 or number % 3 == 0:
        is_prime = False
    else:
        is_prime = True
        for i in range(5,math.isqrt(number),6):
             if number % i == 0 or number % (i + 2) == 0:
                is_prime = False
                break
    prime(is_prime)

def prime(prime_check):
    if prime_check:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)