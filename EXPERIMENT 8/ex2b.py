with open("numbers.txt", "r") as f:
    nums = [int(x.strip()) for x in f]

print("Maximum:", max(nums))