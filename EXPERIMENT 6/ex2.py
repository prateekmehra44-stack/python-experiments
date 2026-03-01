n = int(input("Enter number of values: "))
numbers = []

for i in range(n):
    num = float(input())
    numbers.append(num)

t = tuple(numbers)

avg = sum(t) / len(t)

print("Average:", avg)