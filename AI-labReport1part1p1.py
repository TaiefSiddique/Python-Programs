def find_largest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    largest = find_largest(num1, num2)

    print("The largest number is:", largest)

if __name__ == "__main__":
    main()
