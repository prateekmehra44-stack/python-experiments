nums = list(map(int, input("Enter numbers: ").split()))

result = (lambda lst: (max(lst), min(lst)))(nums)

print(result)