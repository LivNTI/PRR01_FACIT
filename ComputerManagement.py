available_computers = ["IBM PC", "Macintosh","Ataarii", "HP Proobok", "MacBook Air"]

computer_on_service=[]

counter=0
while (counter < 3):
    print(f"You have the following computers:")
    
    for i in range(0,len(available_computers)):
        print(f"{i+1}) {available_computers[i]}")
        
    answer= int(input("which computer do you want to send to servis?"))-1

    computer= available_computers[answer]
    computer_on_service.append(computer)
    available_computers.pop(answer)

    print(f"The following computers are now available:")
    print(available_computers)
    print(f"The following computers are now on service:")
    print(computer_on_service)
    
    counter+=1
