def count(numbers):
    evenCount = 0
    oddCount = 0
    for num in numbers:
        if num % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    return evenCount, oddCount


numbers = []
n = int(input("Enter the number of elements in the list: "))
print("Enter the elements:")
for i in range(n):
    num = int(input())
    numbers.append(num)

evenCount, oddCount = count(numbers)

print("Even numbers:", evenCount)
print("Odd numbers:", oddCount)
