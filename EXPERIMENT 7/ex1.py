def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    return maximum, minimum

nums = list(map(int, input("Enter numbers: ").split()))
result = find_max_min(nums)
print("Maximum:", result[0])
print("Minimum:", result[1])