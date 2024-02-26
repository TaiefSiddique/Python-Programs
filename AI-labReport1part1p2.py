def sum_of_numbers(*args):
    """
    This function takes any number of arguments and returns their sum.
    """
    total = 0
    for num in args:
        total += num
    return total

def main():
    # Example usage of the sum_of_numbers function
    result = sum_of_numbers(1, 2, 3, 4, 5)
    print("Sum of the numbers is:", result)

if __name__ == "__main__":
    main()
