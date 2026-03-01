with open("city.txt", "r") as f:
    for line in f:
        data = line.split()
        if float(data[1]) > 10:
            print(data[0])