try:
    filename = input("Enter file name: ")
    f = open(filename, "r")
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except IOError:
    print("Input Output error occurred")
except Exception as e:
    print("Error:", e)