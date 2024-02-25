def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

def main():
    numbers = []
    n = int(input("Enter the number of elements in the list: "))
    print("Enter the elements:")
    for i in range(n):
        num = int(input())
        numbers.append(num)

    even_count, odd_count = count_even_odd(numbers)

    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)

if __name__ == "__main__":
    main()
