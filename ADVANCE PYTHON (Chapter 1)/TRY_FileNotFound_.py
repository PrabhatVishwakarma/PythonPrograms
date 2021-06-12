def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"{filename} not found")

readFile("File1.txt")
readFile("File2.txt")
readFile("File3.txt")
