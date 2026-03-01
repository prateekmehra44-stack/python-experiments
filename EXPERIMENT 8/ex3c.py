total_area = 0

with open("city.txt", "r") as f:
    for line in f:
        data = line.split()
        total_area += float(data[2])

print("Total area:", total_area)