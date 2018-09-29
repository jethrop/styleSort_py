def styleselect(daytype):
    import random
    #Clothing Database

    #Clothing Variables
    ptrn = ["Plaid ", "Hawaiian "]
    color = ["Blue", "Green", "Red", "Yellow", "Maroon", "Tan", "Brown", "Black", "Grey", "White"]
    colorVariant = ["Light ", "Dark ", "Navy "]
    fabric = ["Jean ", "Cotton ", "Polyester "]
    cut = ["Polo ", "T-shirt ", "Button-up "]

    #Clothing types
    nicepants = [ color[6], color[8], color[7], color[5]]
    allpants = [nicepants, (fabric[0] + color[0])]
    niceshirts = [ cut[2] + color[4], (ptrn[0] + cut[2] + color[2]), cut[2] + color[9], (ptrn[1] + cut[2] + color[1]), (colorVariant[0] + cut[2] + color[0]) ]
    allshirts = [niceshirts]
    shoes = ["black", "brown"]
    church = 0
    casual = 1
    allshoes = [shoes]
    #Test database
    """
    print(nicepants)
    print(allpants)
    print(niceshirts)
    print(allshirts)
    """
    #Selects style for the day

    if daytype == church:
        #Choses clothes
        pantchoice  = (random.choice(nicepants))
        shirtchoice = (random.choice(niceshirts))
        shoechoice = (random.choice(shoes))
        return "Pant type " + pantchoice
        return "Shirt type " + shirtchoice
        print("Shoe type " + shoechoice)
        print("Church")
    elif daytype == casual:
        pantchoice = (random.choice(allpants))
        shirtchoice = (random.choice(allshirts))
        print("Pant type " + pantchoice)
        print("Shirt type " + shirtchoice)
        print("Casual")
    else:
        print("Wrong input")

#runs function
styleselect(0)
styleselect(1)
styleselect("ljlk")
