with open(r"ict.txt", "r") as f:
    lines = f.readlines()

print("Lines:", len(lines))
print("Words:", sum(len(line.split()) for line in lines))
print("Characters:", sum(len(line) for line in lines))