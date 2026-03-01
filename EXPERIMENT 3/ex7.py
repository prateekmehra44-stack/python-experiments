day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

days = [31,28,31,30,31,30,31,31,30,31,30,31]

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days[1] = 29

day = day + 1

if day > days[month-1]:
    day = 1
    month = month + 1
    if month > 12:
        month = 1
        year = year + 1

print("Next Date:")
print("day =", day)
print("month =", month)
print("year =", year)