def vowelFunc(string):
    i = 0
    a = string.lower()
    for x in a:
        if x == "a":
            i = i + 1
        if x == "e":
            i = i + 1
        if x == "i":
            i = i + 1
        if x == "o":
            i = i + 1
        if x == "u":
            i = i + 1
    print(i)


vowelFunc("australopItecUs")