def credCard(string):
    a = string[-4:]
    b = string[:-4]
    for x in b:
        b = b.replace(x, "*")
    
    c =  b + a
    print(c)

credCard("222444008899987")