with open("numbers.txt", "w") as f:
    n = int(input("Enter count of numbers: "))
    for i in range(n):
        num = input()
        f.write(num + "\n")