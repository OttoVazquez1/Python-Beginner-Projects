def Calculator(Numb1, Op, Numb2):
    if type(Numb1) != int or type(Numb2) != int and type(Op) != str:
        print("Error! Use an integrer instead")
    else:
        if Op == "+":
            result = Numb1 + Numb2
            resStr = str(result)
            print("This is your result! " + resStr + " Hope it helped :)")
        elif Op == "-":
            result = Numb1 - Numb2
            resStr = str(result)
            print("This is your result! " + resStr + " Hope it helped :)")
        elif Op == "/":
            result = Numb1 / Numb2
            resStr = str(result)
            print("This is your result! " + resStr + " Hope it helped :)")
        elif Op == "*":
            result = Numb1 * Numb2
            resStr = str(result)
            print("This is your result! " + resStr + " Hope it helped :)")
        else:
            print("Error! Please check your inputs")

print("Welcome to the Calculatortron - 3000")
fn = input("What should the first number be? ")
fnInt = int(fn)
sn = input("Hmm. Good choice.. Now to the second one! ")
snInt = int(sn)
op = input("WOW! Now what's it gonna be? Addition \"+\", substraction \" - \", multiplication \" * \", or division maybe \" / \" ")
opStr = str(op)
Calculator(fnInt, opStr, snInt)