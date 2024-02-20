print("---Menu---")
print("1. Sum")
print("2. Sub")
print("3. Mul")
print("4. Div")

ch = int(input())

if ch == 1:
    print("Sum")
    val1 = int(input("Enter the first value: "))
    val2 = int(input("Enter the second value: "))
    print("Result:", val1 + val2)
elif ch == 2:
    print("Sub")
    val1 = int(input("Enter the first value: "))
    val2 = int(input("Enter the second value: "))
    print("Result:", val1 - val2)
elif ch == 3:
    print("Mul")
    val1 = int(input("Enter the first value: "))
    val2 = int(input("Enter the second value: "))
    print("Result:", val1 * val2)
elif ch == 4:
    print("Div")
    val1 = int(input("Enter the first value: "))
    val2 = int(input("Enter the second value: "))
    if val2 != 0:
        print("Result:", val1 / val2)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid choice")
