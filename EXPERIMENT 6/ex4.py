n = int(input("Enter number of persons: "))
data = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    data[name] = city

print("Names:")
for name in data.keys():
    print(name)

print("Cities:")
for city in data.values():
    print(city)

print("Students and Cities:")
for name, city in data.items():
    print(name, "-", city)

city_count = {}
for city in data.values():
    city_count[city] = city_count.get(city, 0) + 1

print("Number of students in each city:")
for city, count in city_count.items():
    print(city, "-", count)