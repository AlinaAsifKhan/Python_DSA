with open("text.txt", "w+") as f:
    f.write("I deleted the old content\n")
    f.seek(0)
    print(f.read())