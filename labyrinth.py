#this defines how the enterance works
def entrance():
    #set upp the room
    print("you look around the room.")
    print("There is a breeze coming from the stairs to the east.")
    print("to the norht there is a door ther is a warm light from under the door")
    print("choose your path")
    print("1) go down the stairs")
    print("2) go though the door")
    print("3) rest for a bit")
    
    
    choice= input() #get input
    if choice == "1":
        observatory()
    elif(choice == "2"):
        livingroom()
    else:
        print("you decide to rest for a bit")
        entrance()

#defines the livingroom
def livingroom():
    print("you enter a dark room. in the middle there is a fireplace.")
    print("you look to the south and you see a closed door")
    print("to the west you see a window where the sun in shining")
    print("to the east there are stairs going down")
    print("to the north you see a gate, it looks locked")
    print("choose your path")
    print("1) go down the stairs")
    print("2) check out the gate")
    print("3) look out the window")
    print("4) try the door")

    choice= input() #get input
    if choice == "1":
        observatory()
    elif(choice == "2"):
        exit()
    elif(choice == "3"):
        print("You look out the windobw and see dark clouds and lightning in the distance")
        livingroom()
    elif(choice == "4"):
        enterance()
    else:
        print("you decide to rest for a bit")
        livingroom()
    
    #defines the observatory
    def observatory():
        print("you look around")
        print("there is a big open room and you see stars above")
        print('"This is odd" you think to your self "It was day just minutes ago"')
        print("you look behind you and see two sets of stairs")
        print("choose your path")
        print("1) go up the stairs to the left")
        print("2) go up the stairs to the right")
        
        choice= input() #get input
        if choice == "1":
            entrance()
        elif(choice == "2"):
            livingroom()
        else:
            observatory()
    
    #defines the exit
    def exit():
        print("you approach the gate and rattle the lock")
        print("to your surprise the chain is rusted and disintegrates in your hands.")
        print("You sprint out the gate before something else can happen and leace the house behind you")
    
    #main code
    print ("You find yourself in a forest")
    print("as you walk along the path you come acroos a cottage in a sunny clearing")
    print("the door is open and you decide to look inside")
    print("as you enter the door closes behind you")
    entrance()