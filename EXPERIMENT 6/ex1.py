n = int(input("Enter number of values: "))
values = []

for i in range(n):
    num = int(input())
    values.append(num)

for i in range(4):
    print(i, "occurs", values.count(i), "times")