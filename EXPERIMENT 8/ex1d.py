longest = ""

with open("name.txt", "r") as f:
    for line in f:
        name = line.strip()
        if len(name) > len(longest):
            longest = name

print("Longest name:", longest)