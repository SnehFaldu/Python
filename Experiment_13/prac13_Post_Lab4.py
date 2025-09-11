with open(r"file1.txt", "r") as f1, open(r"file2.txt", "r") as f2, open(r"merged.txt", "w") as mf:
    # Write contents of file1 first
    mf.write(f1.read())
    mf.write("\n")  # optional newline between files
    # Then write contents of file2
    mf.write(f2.read())