import math
from numba import jit

@jit
def is_prime_number(number):
    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def main():
    user_input = int(input("Enter a positive integer: "))

    prime_number_count = 0
    number = 2
    while prime_number_count < user_input:
        is_prime = is_prime_number(number)
        if is_prime:
            prime_number_count += 1
            print(f"{prime_number_count}: {number}")
        number += 1

if __name__ == "__main__":
    main()