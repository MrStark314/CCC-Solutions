Totalplyers = int(input("Number of players: "))
Starplayers = 0

for i in range(Totalplyers):
    Numberofpoints = int(input("Number of goals: "))
    Numberoffouls = int(input("Number of fouls: "))
    Numberofstars = Numberofpoints * 5 - Numberoffouls * 3
    if Numberofstars > 40:
        Starplayers = Starplayers + 1 

if Starplayers == Totalplyers:
    print(str(Starplayers) + '+')
else:
    print(Starplayers)
10

        


