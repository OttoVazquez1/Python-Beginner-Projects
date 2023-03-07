lista = [1, 3, 7, 5, 15, 22, 45, 13, 2712, 559, 72]
def listchallenge(string, numbList):
    listaMod = numbList.copy()
    if  string == "none":
        print(numbList)
    elif string == "desc":
        listaMod.sort(reverse = True)
        print(listaMod)
    elif string == "asc":
        listaMod.sort()
        print(listaMod)


params = ["asc", "none", "desc"]

i = 0 

while i < len(params):
    listchallenge(params[i], lista)
    i = i + 1