#this defines how the enterance works
def entrance():
    #set upp the room
    print("you look around the room.")
    print("There is a breeze coming from the stairs to the south.")
    print("to the norht there is a door ther is a warm light from under the door")
    print("choose your path")
    print("1) go down the stairs")
    print("2) go though the door")
    print("3) rest for a bit")
    
    
    choice= input() #get input
    if choice == "1":
        livingroom()
    elif(choice == 2):
        observatory()
    else:
        print("you decide to rest for a bit")
        entrance()
        
def living room
    
    