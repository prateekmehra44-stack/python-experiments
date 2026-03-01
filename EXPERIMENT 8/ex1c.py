count = 0

with open("name.txt", "r") as f:
    for line in f:
        if line.strip()[0].lower() in "aeiou":
            count += 1

print("Names starting with vowel:", count)