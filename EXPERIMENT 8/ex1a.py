with open("name.txt", "w") as f:
    n = int(input("Enter number of names: "))
    for i in range(n):
        name = input()
        f.write(name + "\n")