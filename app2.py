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
                print(i)
                numbers.remove(i)
    
    print(numbers)

if __name__ == "__main__":
    main()
