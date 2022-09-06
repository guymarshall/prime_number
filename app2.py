# import math


# def is_prime_number(number):
#     for i in range(2, math.ceil(math.sqrt(number)) + 1):
#         if number % i == 0:
#             return False
#     return True


# def main():
#     user_input = int(input("Enter a positive integer: "))

#     prime_number_count = 0
#     number = 2
#     while prime_number_count < user_input:
#         is_prime = is_prime_number(number)
#         if is_prime:
#             prime_number_count += 1
#             print(f"{prime_number_count}: {number}")
#         number += 1


# if __name__ == "__main__":
#     main()

def generate_list(number):
    numbers = []

    for i in range(1, number + 1):
        numbers.append(i)
    
    return numbers

def main():
    user_input = int(input("Enter a positive integer: "))
    numbers = generate_list(user_input)

    for number in numbers:
        for i in numbers:
            if i != number and i % number == 0:
                numbers.remove(i)
    
    print(numbers)

if __name__ == "__main__":
    main()
