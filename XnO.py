def xo(string):
    ex = 0
    os = 0
    stringLower = string.lower()
    for x in stringLower:
        if x == "x":
            ex = ex + 1
        if x == "o":
            os = os + 1
    print(os)
    print(ex)

    if os == ex:
        print(True)
    elif os != ex:
        print(False)
    elif os == 0 and ex == 0:
        print(True)
    

x = input("Insert X's and O's: ")

xo(x)