with open("name.txt", "r") as f:
    names = f.readlines()

print("Total names:", len(names))