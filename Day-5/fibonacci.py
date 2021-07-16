numbers = []


numbers.insert(0,0)
numbers.insert(1,1)

for i in range(2, 10):
    next = numbers[i- 2] + numbers[i - 1]
    numbers.append(next)

print(numbers)

