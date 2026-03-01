count = 0
with open("numbers.txt", "r") as f:
    numbers = [int(x.strip()) for x in f]

for num in numbers:
    if num > 100:
        count += 1

print("Numbers greater than 100:", count)