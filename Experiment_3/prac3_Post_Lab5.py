str = input("Enter a sentence: ")
words = str.strip().split()
if words:
    last = words[-1]
    print("Length of the last word:", len(last))