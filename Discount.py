def discount(price, discount):
    if type(price) != int and type(discount != int):
        print("Error. Try using an integrer!")
    else:
        discounted = price * discount / 100

        applied = price - discounted
        
        applied = int(applied)

        applied = str(applied)
        
        print("Your discounted price is " + applied)

x = input("Insert the original price: ")
xInt = int(x)
y = input("Insert the percentage discount you'd like: ")
yInt = int(y)
discount(xInt, yInt)