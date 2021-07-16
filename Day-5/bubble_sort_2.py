for i in range(0, len(numbers)): 
    for j in range(0, len(numbers)): 
        #print(f"{numbers[i]} < {numbers[j]}")
        if numbers[i] < numbers[j]: 
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp 