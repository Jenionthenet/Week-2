numbers = [18, 3, 12, 7, 1, 5]

for i in range (0, len(numbers)):

    for j in range (0, len(numbers) -1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j +1]
            numbers[j + 1] = temp

print(numbers)